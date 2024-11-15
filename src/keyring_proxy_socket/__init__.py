from typing import override

from jaraco.classes import properties
from keyring_proxy.backend import ProxyBackend
from keyring_proxy.socketproxy import SocketClient, default_socket_mgr_client
from keyring_proxy.transport import TransportClient

PRIORITY = 9.9


class SocketProxyBackend(ProxyBackend):
    socket_path: str | None = None
    socket_host: str | None = None
    socket_port: str | int | None = None

    @override
    def _get_transport(self) -> TransportClient:
        return SocketClient(default_socket_mgr_client(self.socket_path, self.socket_host, self.socket_port))

    @properties.classproperty
    def priority(cls):
        return PRIORITY
