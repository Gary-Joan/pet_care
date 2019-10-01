from browser import Browser
from selenium import webdriver

def before_all(context):
  context.browser = Browser()


def after_all(context):
  pass