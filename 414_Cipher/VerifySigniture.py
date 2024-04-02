# ATTEMPT 2 IDK WHAT TO DO!
from Crypto.Signature import dilithium
from Crypto.PublicKey import dilithium_params
from Crypto.Hash import SHAKE128
import base64

def verify_dilithium(message, base64_signature, base64_encoded_public_key):
    # Convert ASCII base64-encoded string message to the right hex format
    message_bytes = message.encode('utf-8')
    
    # Import the key
    pub_key = dilithium_params.DilithiumPublicKey.from_bytes(base64.b64decode(base64_encoded_public_key))
    
    # Convert the base64-encoded signature to a byte array needed by the algorithm
    signature_bytes = base64.b64decode(base64_signature)
    
    # Create the Dilithium verifier object
    verifier = dilithium.DilithiumSigner(pub_key)
    
    # Hash the message using SHAKE128
    shake = SHAKE128.new()
    shake.update(message_bytes)
    message_digest = shake.read(32)  # 32 bytes = 256 bits
    
    # Verify the signature
    try:
        verifier.verify(message_digest, signature_bytes)
        print("Signature is valid.")
    except dilithium.DilithiumError:
        print("Signature is invalid.")

# Example usage
message = "Your message here"
base64_signature = "base64-encoded-signature"
base64_encoded_public_key = "base64-encoded-public-key"
verify_dilithium(message, base64_signature, base64_encoded_public_key)
