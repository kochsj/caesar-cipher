import pytest
from caesar_cipher import encrypt, decrypt
import random

def test_encryption():
    org_sent = 'The rain in Spain falls mainly on the plain.'
    expected = 'vjg tckp kp urckp hcnnu ockpna qp vjg rnckp.'
    assert encrypt(org_sent, 2) == expected

def test_decryption_known():
    org_encrypted = 'vjg tckp kp urckp hcnnu ockpna qp vjg rnckp.'
    expected = 'the rain in spain falls mainly on the plain.'
    assert decrypt(org_encrypted) == expected

def test_decrypt_random():
    org_sent = '“i hope that in this year to come, you make mistakes. because if you are making mistakes, then you are making new things, trying new things, learning, living, pushing yourself, changing yourself, changing your world. you’re doing things you’ve never done before, and more importantly, you’re doing something.”'
    encrypted = encrypt(org_sent, random.randint(1,26))
    assert org_sent == decrypt(encrypted)