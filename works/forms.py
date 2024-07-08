import os

from django import forms
from django.conf import settings
from django.forms import ModelForm, Form

from works.models import *

from django import forms


# class fileInfoForm(ModelForm):
#     """
#     图书表单
#     """
#
#     class Meta:
#         model = Book()
#         fields = '__all__'
#         widgets = {
#             'file': forms.TextInput(attrs={'id': 'file', 'class': 'inputClass'}),
#             'filename': forms.TextInput(attrs={'id': 'filename'})
#         }
#         labels = {
#             'file': '文章内容',
#             'filename': "文章名字"
#         }
    # publishDate = forms.DateField(label="出版日期")
    # 图书类别列表
    # bookTypeList=BookTypeInfo.objects.values()
    # 图书类别以下拉框形式显现，下拉框选项是图书类别Id,下拉框选项文本是图书类别名称
    #  choises = [(v['id'],v['bookTypeName']) for v, v in enumerate(bookTypeList)]
    # bookType=forms.ChoiceField(choises=choises, label="图书类别")

#
# class photoForm(ModelForm):
#     class Meta:
#         model = photo()
#         file_path=os.path.join(settings.BASE_DIR, '/media')
#         fields = '__all__'
#         widgets = {
#             'photo': forms.ImageField(upload_to='file_path',allow_empty_file=False)
#         }
#         labels = {
#             'photo': '图片'
#         }


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'image']

class fileInfoForm(Form):
    """
    图书表单
    """
    filename=forms.CharField(max_length=20,label="文章名称")
    file=forms.CharField(label="文章内容")