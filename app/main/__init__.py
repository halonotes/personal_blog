# coding:utf-8
# 创建蓝本
from flask import Blueprint

main = Blueprint('main', __name__)
# 实例化Blueprint类用于创建蓝本
# 参数一：蓝本的名字；参数二：蓝本所在的包或模块

from . import views, errors
from ..models import Permission


@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)
