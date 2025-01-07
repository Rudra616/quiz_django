from django.db import models
import random
import uuid
# Create your models here.
class BaseModel(models.Model):
    uid =models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

class Category(BaseModel):
    category_name =models.CharField(max_length=100)
    
    def __str__(self):
        return self.category_name
    

class Question(BaseModel):
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    marks = models.IntegerField(default=5)

    def __str__(self):
        return self.question

    def get_answers(self):
        answer_objs = list(Ans.objects.filter(question=self))
        data = []
        random.shuffle(answer_objs)
        for answer_obj in answer_objs:
            data.append({
                "answer": answer_obj.ans,
                "is_correct": answer_obj.iscorrect
            })
        return data

class Ans(BaseModel):
    
    question = models.ForeignKey(Question,related_name='answers',on_delete=models.CASCADE)
    ans=models.CharField(max_length=100)
    iscorrect = models.BooleanField(default=False)

    def __str__(self):
        return self.ans

