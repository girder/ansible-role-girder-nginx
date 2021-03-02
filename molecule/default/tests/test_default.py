import os

import pytest


def test_nginx_install(host):
    nginx_package = host.package('nginx-light')
    assert nginx_package.is_installed


def test_nginx_default_config_removed(host):
    nginx_default_config = host.file('/etc/nginx/sites-enabled/default')
    assert not nginx_default_config.exists


@pytest.mark.parametrize('config_name', [
    'base.conf',
    'girder.conf'
])
def test_nginx_config_exists(host, config_name):
    config_path = os.path.join('/etc/nginx/conf.d', config_name)
    nginx_config = host.file(config_path)
    assert nginx_config.is_file
    assert nginx_config.user == 'root'
    assert nginx_config.group == 'root'


def test_nginx_service(host):
    nginx_service = host.service('nginx')
    assert nginx_service.is_running
    assert nginx_service.is_enabled


@pytest.mark.parametrize('socket', [
    80,
    443
])
def test_nginx_socket(host, socket):
    nginx_socket = host.socket(f'tcp://0.0.0.0:{socket}')
    assert nginx_socket.is_listening
