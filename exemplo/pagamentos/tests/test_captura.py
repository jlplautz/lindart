import pytest
import responses
from django.urls import reverse


TOKEN = 'test_transaction_nORKaWFnz3wsUAXHInUsB9tLEszW02'


@pytest.fixture
def test_pagarme_responses():
    with responses.RequestsMock() as rsps:
        rsps.add(responses.GET, f'https://api.pagar.me/1/transactions/{TOKEN}', json=transaction_resp)
        rsps.add(responses.POST, f'https://api.pagar.me/1/transactions/{TOKEN}/capture', json=captura_resp)
        yield rsps


@pytest.fixture
def resp(client, test_pagarme_responses):
    return client.post(reverse('pagamentos:captura'), {'token': TOKEN})


def test_status_code(resp):
    assert resp.status_code == 200


@pytest.fixture
def test_pagarme_invalid_responses():
    with responses.RequestsMock() as rsps:
        rsps.add(responses.GET, f'https://api.pagar.me/1/transactions/{TOKEN}', json=transaction_resp_menor_que_minimo)
        yield rsps


@pytest.fixture
def resp_invalido(client, test_pagarme_invalid_responses):
    return client.post(reverse('pagamentos:captura'), {'token': TOKEN})


def test_status_code_invalido_value(resp_invalido):
    assert resp_invalido.status_code == 400


transaction_resp = {
    'object': 'transaction', 'status': 'authorized', 'refuse_reason': None, 'status_reason': 'antifraud',
    'acquirer_response_code': '0000', 'acquirer_name': 'pagarme', 'acquirer_id': '5e1db60d3d9e4e2947286920',
    'authorization_code': '928705', 'soft_descriptor': None, 'tid': 7670664, 'nsu': 7670664,
    'date_created': '2020-01-23T02:13:37.172Z', 'date_updated': '2020-01-23T02:13:37.441Z', 'amount': 8000,
    'authorized_amount': 8000, 'paid_amount': 0, 'refunded_amount': 0, 'installments': 1, 'id': 7670664, 'cost': 70,
    'card_holder_name': 'fooxiv', 'card_last_digits': '1111', 'card_first_digits': '411111', 'card_brand': 'visa',
    'card_pin_mode': None, 'card_magstripe_fallback': False, 'cvm_pin': False, 'postback_url': None,
    'payment_method': 'credit_card', 'capture_method': 'ecommerce', 'antifraud_score': None, 'boleto_url': None,
    'boleto_barcode': None, 'boleto_expiration_date': None, 'referer': 'encryption_key', 'ip': '189.4.30.184',
 }

transaction_resp_menor_que_minimo = {
    'object': 'transaction', 'status': 'authorized', 'refuse_reason': None, 'status_reason': 'antifraud',
    'acquirer_response_code': '0000', 'acquirer_name': 'pagarme', 'acquirer_id': '5e1db60d3d9e4e2947286920',
    'authorization_code': '928705', 'soft_descriptor': None, 'tid': 7670664, 'nsu': 7670664,
    'date_created': '2020-01-23T02:13:37.172Z', 'date_updated': '2020-01-23T02:13:37.441Z', 'amount': 800,
    'authorized_amount': 800, 'paid_amount': 0, 'refunded_amount': 0, 'installments': 1, 'id': 7670664, 'cost': 70,
    'card_holder_name': 'fooxiv', 'card_last_digits': '1111', 'card_first_digits': '411111', 'card_brand': 'visa',
    'card_pin_mode': None, 'card_magstripe_fallback': False, 'cvm_pin': False, 'postback_url': None,
    'payment_method': 'credit_card', 'capture_method': 'ecommerce', 'antifraud_score': None, 'boleto_url': None,
    'boleto_barcode': None, 'boleto_expiration_date': None, 'referer': 'encryption_key', 'ip': '189.4.30.184',
 }


captura_resp = {
    'object': 'transaction', 'status': 'paid', 'refuse_reason': None, 'status_reason': 'acquirer',
    'acquirer_response_code': '0000', 'acquirer_name': 'pagarme', 'acquirer_id': '5e1db60d3d9e4e2947286920',
    'authorization_code': '7909', 'soft_descriptor': None, 'tid': 7670888, 'nsu': 7670888,
    'date_created': '2020-01-23T04:38:29.182Z', 'date_updated': '2020-01-23T04:45:01.928Z',
    'amount': 8000, 'authorized_amount': 8000, 'paid_amount': 8000, 'refunded_amount': 0, 'installments': 1,
    'id': 7670888, 'cost': 120, 'card_holder_name': 'fooxv', 'card_last_digits': '1111', 'card_first_digits': '411111',
    'card_brand': 'visa', 'card_pin_mode': None, 'card_magstripe_fallback': False, 'cvm_pin': False,
    'postback_url': None, 'payment_method': 'credit_card', 'capture_method': 'ecommerce', 'antifraud_score': None,
    'boleto_url': None, 'boleto_barcode': None, 'boleto_expiration_date': None, 'referer': 'encryption_key',
    'ip': '189.4.30.184',
}
