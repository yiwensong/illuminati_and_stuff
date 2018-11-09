from unittest import mock

import pyramid.config
import pyramid.tweens
import pytest

import illuminati_and_stuff


@pytest.fixture
def fake_config():
    config = pyramid.config.Configurator()
    with mock.patch.object(config, 'add_tween'):
        yield config


def test_includeme(fake_config):
    illuminati_and_stuff.includeme(fake_config)
    fake_config.add_tween.assert_called_with(
        'illuminati_and_stuff.tween_factory.IlluminatiAndStuffTweenFactory',
        over=pyramid.tweens.MAIN,
    )
