from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'checkout'

    def ready(self) -> None:
        import checkout.signals
