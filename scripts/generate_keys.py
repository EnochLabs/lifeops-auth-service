import os

import rsa


def generate_keys(directory: str = "secrets"):
    """Generates RSA public and private keys."""
    os.makedirs(directory, exist_ok=True)

    priv_path = os.path.join(directory, "jwt_private_key.pem")
    pub_path = os.path.join(directory, "jwt_public_key.pem")

    if os.path.exists(priv_path) or os.path.exists(pub_path):
        print(f"Keys already exist in {directory}. Skipping generation.")
        return

    print(f"Generating 2048-bit RSA keys in {directory}...")
    pubkey, privkey = rsa.newkeys(2048)

    with open(priv_path, "wb") as f:
        f.write(privkey.save_pkcs1("PEM"))

    with open(pub_path, "wb") as f:
        f.write(pubkey.save_pkcs1("PEM"))

    print(f"Private key saved to: {priv_path}")
    print(f"Public key saved to: {pub_path}")


if __name__ == "__main__":
    generate_keys()
