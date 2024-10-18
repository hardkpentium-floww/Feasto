from feasto_core_clean_arch.interactors.storage_interfaces.storage_interface import StorageInterface


class AddItemInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage
