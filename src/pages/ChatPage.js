// ChatPage.js

import React, { useEffect, useRef, useState, useCallback, useMemo } from 'react';
import { animateScroll } from 'react-scroll';
import { useLocation, useNavigate } from 'react-router-dom';
import './ChatPage.css';
import useConversation from '../hooks/useConversation.js';
import MessageInput from '../components/MessageInput.js';
import Message from '../components/Message.js';

function ChatPage() {
    const location = useLocation();
    const navigate = useNavigate();
    const inputQuery = location.state?.query;

    const {
        messages,
        handlePrimary,
        handleAuxiliary,
        isSending
    } = useConversation();

    const sentRef = useRef(false);

    // **Maintain the display state of each round**
    const [displayedBotMessageCounts, setDisplayedBotMessageCounts] = useState([]);
    const [isAuxiliaryLoading, setIsAuxiliaryLoading] = useState(false);

    // When the component mounts and there's an input query, send the initial query
    useEffect(() => {
        if (inputQuery && !sentRef.current) {
            handlePrimary(inputQuery);
            sentRef.current = true;
        }
    }, [inputQuery, handlePrimary]);

    // When there are new messages, scroll to the bottom of the chat messages
    useEffect(() => {
        if (messages.length > 0) {
            animateScroll.scrollToBottom({
                containerId: 'chatbot-messages',
                duration: 100,
            });
        }
    }, [messages]);

    // **Group messages into conversation rounds**
    const rounds = useMemo(() => {
        const rounds = [];
        let currentRound = null;

        messages.forEach((msg) => {
            if (msg.from === 'user') {
                if (currentRound) {
                    rounds.push(currentRound);
                }
                currentRound = {
                    messages: [],
                    totalBotMessages: 0,
                };
            }
            if (!currentRound) {
                currentRound = {
                    messages: [],
                    totalBotMessages: 0,
                };
            }
            currentRound.messages.push(msg);

            if (msg.from === 'bot') {
                currentRound.totalBotMessages += msg.messages.length;
            }
        });

        if (currentRound) {
            rounds.push(currentRound);
        }

        return rounds;
    }, [messages]);

    // **Synchronize displayedBotMessageCounts with the length of rounds**
    useEffect(() => {
        setDisplayedBotMessageCounts((prevCounts) => {
            const newCounts = [...prevCounts];
            while (newCounts.length < rounds.length) {
                newCounts.push(1); // Initialize to show 1 bot message per round
            }
            return newCounts.slice(0, rounds.length);
        });
    }, [rounds.length]);

    // **Handle the "show more/show less" functionality for each round**
    const handleToggle = useCallback(
        (roundIndex) => async () => {
            setDisplayedBotMessageCounts((prevCounts) => {
                const newCounts = [...prevCounts];
                const displayedBotMessageCount = newCounts[roundIndex];
                const totalBotMessages = rounds[roundIndex].totalBotMessages;

                if (displayedBotMessageCount < totalBotMessages) {
                    newCounts[roundIndex] = displayedBotMessageCount + 1;
                } else {
                    newCounts[roundIndex] = 1;
                }

                return newCounts;
            });

            // If displaying all, need to load auxiliary messages (only for the last round)
            if (
                displayedBotMessageCounts[roundIndex] + 1 >= rounds[roundIndex].totalBotMessages &&
                !isSending &&
                roundIndex === rounds.length - 1
            ) {
                setIsAuxiliaryLoading(true);
                try {
                    await handleAuxiliary();
                } catch (error) {
                    console.error('Error loading auxiliary messages:', error);
                } finally {
                    setIsAuxiliaryLoading(false);
                }
            }
        },
        [displayedBotMessageCounts, rounds, isSending, handleAuxiliary]
    );

    // **Get the button text for each round**
    const getButtonText = (roundIndex) => {
        const displayedBotMessageCount = displayedBotMessageCounts[roundIndex] || 1;
        const totalBotMessages = rounds[roundIndex].totalBotMessages;

        if (isAuxiliaryLoading && roundIndex === rounds.length - 1) {
            return 'Generating the next reply...';
        } else if (displayedBotMessageCount >= totalBotMessages) {
            return 'Collapse excess information';
        } else {
            return 'Show more';
        }
    };

    // **Prepare messages to be displayed**
    const displayedMessages = useMemo(() => {
        const result = [];

        rounds.forEach((round, roundIndex) => {
            let botMessageCount = 0;
            const displayedBotMessageCount = displayedBotMessageCounts[roundIndex] || 1;

            // **Sort bot messages**
            const sortedBotMessages = [];
            round.messages.forEach((msgGroup) => {
                if (msgGroup.from === 'bot') {
                    sortedBotMessages.push(...msgGroup.messages);
                }
            });

            // Sort bot messages by `order` attribute
            sortedBotMessages.sort((a, b) => a.order - b.order);

            // Clip the bot messages to be displayed
            const botMessagesToDisplay = sortedBotMessages.slice(0, displayedBotMessageCount);

            // Rebuild bot message groups
            const botMessageGroups = [];
            botMessagesToDisplay.forEach((message) => {
                if (
                    botMessageGroups.length === 0 ||
                    botMessageGroups[botMessageGroups.length - 1].from !== 'bot'
                ) {
                    botMessageGroups.push({
                        from: 'bot',
                        messages: [message],
                        roundIndex,
                        startIndex: 0,
                    });
                } else {
                    botMessageGroups[botMessageGroups.length - 1].messages.push(message);
                }
            });

            // Combine user messages and bot message groups
            round.messages.forEach((msgGroup) => {
                if (msgGroup.from === 'user') {
                    result.push({ ...msgGroup, roundIndex, startIndex: 0 });
                }
            });

            result.push(...botMessageGroups);
        });

        return result;
    }, [rounds, displayedBotMessageCounts]);

    // If there is no input query, navigate back to the homepage
    useEffect(() => {
        if (!inputQuery) {
            navigate('/');
        }
    }, [inputQuery, navigate]);

    return (
        <div className="chatbot-container">
            <div id="chatbot-messages" className="chatbot-messages">
                {displayedMessages.map((msg, index) => {
                    const isLastBotMessageInRound =
                        msg.from === 'bot' &&
                        (index === displayedMessages.length - 1 ||
                            (displayedMessages[index + 1] &&
                                displayedMessages[index + 1].roundIndex !== msg.roundIndex));

                    return (
                        <Message
                            key={index}
                            messages={msg.messages}
                            from={msg.from}
                            startIndex={msg.startIndex}
                            isSending={isSending}
                            handleToggle={
                                isLastBotMessageInRound
                                    ? handleToggle(msg.roundIndex)
                                    : null
                            }
                            buttonText={
                                isLastBotMessageInRound
                                    ? getButtonText(msg.roundIndex)
                                    : null
                            }
                        />
                    );
                })}
            </div>
            <MessageInput onSendMessage={handlePrimary} isSending={isSending} />
        </div>
    );
}

export default ChatPage;
