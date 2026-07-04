from whitenoise.storage import CompressedManifestStaticFilesStorage


class SilentCompressedManifestStaticFilesStorage(CompressedManifestStaticFilesStorage):
    """
    Igual que CompressedManifestStaticFilesStorage, pero no falla si algún
    archivo (como un .map de una librería de terceros) no se encuentra.
    """
    manifest_strict = False