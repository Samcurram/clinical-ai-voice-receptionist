import asyncio
import logging
from typing import Dict, Any

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ClinicalVoiceReceptionist")

class ClinicVoiceAgent:
    def __init__(self, clinic_name: str = "Dental Care Clinic"):
        self.clinic_name = clinic_name
        logger.info(f"Initialized {self.clinic_name} AI Voice Receptionist Agent.")

    async def process_call(self, caller_phone: str, transcript: str) -> Dict[str, Any]:
        logger.info(f"Processing incoming call from {caller_phone}: \"{transcript}\"")
        
        # Simulated extraction of intent and slot booking using structured tool calling
        extracted_data = {
            "patient_name": "Rahul Sharma",
            "phone_number": caller_phone,
            "requested_slot": "2026-11-18T10:30:00",
            "service": "Dental Consultation",
            "status": "confirmed"
        }
        
        logger.info(f"Successfully booked appointment: {extracted_data}")
        return extracted_data

if __name__ == "__main__":
    agent = ClinicVoiceAgent()
    asyncio.run(agent.process_call("+919515322073", "Namaste, I want to book a dental checkup slot for Tuesday morning."))
