from django.urls import converters, register_converter


class CategoryConverter(object):
    regex = r'\w+|(\w+\+\w+)+)+'

    # 将/article/python+gp+ruby 编程['python','gp','ruby']

    def to_python(self, value):
        result = value.split("+")
        return result

    # reverse 通过反转获取url 需要将列表转成python+gp+ruby
    def to_url(self, value):
        if isinstance(value, list):
            result = "+".join(value)
            return result
        else:
            raise RecursionError("转化url的时候参数必须为列表")


register_converter(CategoryConverter, 'cate')
