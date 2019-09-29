
from behave import given, when, then
from selenium import *
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from django.test.client import Client
from behave   import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select
###################################################################mostrar login pagina############################################
@given(u'user is on home page')
def step_impl(context):
    context.browser.visit()

@when(u'user click on "LOGIN"')
def step_impl(context):
    context.browser.visit('#')


@when(u'user click on  "LOGIN CLIENTE"')
def step_impl(context):
    context.browser.visit('login/')
################################################################### ingresar datos login############################################

@then(u'user can see login page')
def step_impl(context):
    #response = context.browser.client.get('login/')
    #context.assertTemplateUsed(response, 'register.html')
    pass
@given(u'user is on login page')
def step_impl(context):
    context.browser.visit('login/')


@when(u'user fill "username" with "{user}"')
def step_impl(context, user):
    username = context.browser.driver.find_element_by_name('username')
    username.send_keys(user)


@when(u'user fill "password" with "{passw}"')
def step_impl(context,passw):
    password = context.browser.driver.find_element_by_name('password')
    password.send_keys(passw)


@then(u'user will redirect to home page')
def step_impl(context):
    context.browser.driver.find_element_by_name('login').click()

################################################################### ingresar datos login############################################


@when(u'user type "{page}" on browser')
def step_impl(context, page):
    context.browser.visit(page)

@when(u'user go the username option')
def step_impl(context):
    driver = context.browser.driver


@then(u'user click con "pedir cita" option')
def step_impl(context):
    context.browser.visit('event/new/')


@then(u'user see "event.html" page')
def step_impl(context):
    context.browser.find_by_id('id_title')

