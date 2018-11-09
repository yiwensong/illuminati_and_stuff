from illuminati_and_stuff import tween_factory

MAGIC = 'magic'


def fake_handler(*args, **kwargs):
    return MAGIC


def fake_handler_errors(*args, **kwargs):
    raise Exception(MAGIC)


class FakeRegistry:
    pass


class FakeRequest:
    pass


def test_illuminati_and_stuff_tween_factory_success():
    resp = tween_factory.IlluminatiAndStuffTweenFactory(
        fake_handler,
        FakeRegistry(),
    )(FakeRequest())
    assert resp == MAGIC


def test_illuminati_and_stuff_tween_factory_tb():
    resp = tween_factory.IlluminatiAndStuffTweenFactory(
        fake_handler_errors,
        FakeRegistry(),
    )(FakeRequest())
    body = resp.body.decode()
    assert MAGIC in body
    assert 'Exception' in body
