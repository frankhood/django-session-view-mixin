#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-session-mixin-view
------------

Tests for `django-session-mixin-view` models module.
"""
from django.utils import timezone
from django.test import TestCase
# Create your tests here.
from django_session_mixin_view.session_mixin import SessionMixin

# =============================================
# ./manage.py test tests.example.test_views.TestViewSessionMixin
# =============================================
class TestViewSessionMixin(TestCase):

    def setUp(self) -> None:
        self.item_1 = 'value_1'
        self.item_2 = 'value_2'

    # =============================================
    # ./manage.py test tests.example.test_views.TestViewSessionMixin.test_set_session
    # =============================================
    def test_set_session(self):

        session = self.client.session
        session_mixin = SessionMixin()

        with self.subTest('Simple test'):
            session_mixin.set_in_session(session=session, item_1=self.item_1)
            session_mixin.set_in_session(session=session, item_2=self.item_2)

            self.assertEqual(session.get('item_1'), self.item_1)
            self.assertEqual(session.get('item_2'), self.item_2)

        with self.subTest('Expired setter'):
            session_mixin.set_in_session(session=session, item=self.item_1, expires=10)
            self.assertIn('__value', session.get('item'))
            self.assertIn('expires', session.get('item'))

    # =============================================
    # ./manage.py test tests.example.test_views.TestViewSessionMixin.test_get_session
    # =============================================
    def test_get_session(self):
        session = self.client.session

        with self.subTest('Simple test'):

            session['item_1'] = self.item_1
            session['item_2'] = self.item_2
            session.save()

            self.assertEqual(SessionMixin().get_from_session(session=session, key='item_1'), self.item_1)
            self.assertEqual(SessionMixin().get_from_session(session=session, key='item_2'), self.item_2)

        with self.subTest('isinstance(val, dict)'):

            dict_value_with_expired = {
                '__value': 'value_1',
                'expires': 10
            }

            session['item_1'] = dict_value_with_expired
            session.save()

            self.assertEqual(SessionMixin().get_from_session(session=session, key='item_1'),
                             dict_value_with_expired.get('__value'))

            dict_value_without_expired = {
                '__value': 'value_1'
            }
            session['item_1'] = dict_value_without_expired
            session.save()

            self.assertEqual(SessionMixin().get_from_session(session=session, key='item_1'),
                             dict_value_without_expired.get('__value'))

        with self.subTest('Not Exists item in session'):
            raised = False
            try:
                SessionMixin().get_from_session(session=session, key='item_1')
            except Exception:
                raised = True
            self.assertFalse(raised, 'Exception raised')

        with self.subTest('Expired key in session'):
            value = {
                '__value': 'value_1',
                'expires': timezone.now()
            }
            session['item_1'] = value
            self.assertEqual(
                SessionMixin().get_from_session(session=session, key='item_1'),
                None
            )

    # =============================================
    # ./manage.py test tests.example.test_views.TestViewSessionMixin.test_remove_session
    # =============================================
    def test_remove_session(self):

        session = self.client.session

        SessionMixin().set_in_session(session=session, item_1=self.item_1)
        SessionMixin().set_in_session(session=session, item_2=self.item_2)

        with self.subTest('Simple Case'):
            SessionMixin().remove_from_session(session=session, keys=['item_1'])
            self.assertEqual(list(session.keys()), ['item_2'])

            SessionMixin().remove_from_session(session=session, keys=['item_2'])
            self.assertEqual(list(session.keys()), [])

        with self.subTest('Not exists key'):
            raised = False
            try:
                SessionMixin().remove_from_session(session=session, keys=['Not exists'])
            except:
                raised = True
            self.assertFalse(raised, 'Exception raised')
