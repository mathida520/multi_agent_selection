from app.services.task_handler import PICTURE_GENERATION

general=[]
image_generation=[]

def get_model_list(task_type):
    if task_type == PICTURE_GENERATION:
        return image_generation
    else:
        return general

# todo 获取到有哪些模型之后在这里更新模型清单
def set_models(task_type, models):
    if task_type == PICTURE_GENERATION:
        image_generation.extend(models)
    else:
        general.extend(models)