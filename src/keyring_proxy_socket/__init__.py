from typing import override

from jaraco.classes import properties
from keyring_proxy.socketproxy import DEFAULT_SOCKET_PATH, SocketClient
from keyring_proxy.transport import ProxyBackend, TransportClient

PRIORITY = 9.9


class SocketProxyBackend(ProxyBackend):

    socket: str = DEFAULT_SOCKET_PATH

    @override
    def _get_transport(self) -> TransportClient:
        return SocketClient.from_path(self.socket)

    @properties.classproperty
    def priority(cls):
        return PRIORITY
