"""
Simple example/test demonstrating filler-word interruption filtering.
This script simulates interim and final STT events and shows whether the
AgentActivity will ignore filler-only transcripts while an agent is speaking.

Usage: run the script with the same Python environment used by the project.
It does not require audio I/O or external STT/TTS backends.
"""
from __future__ import annotations

import asyncio
import logging
from dataclasses import dataclass

# adapt imports relative to workspace
from livekit.agents.voice.agent_activity import AgentActivity
from livekit.agents.voice.agent_session import AgentSession
from livekit.agents.stt.stt import SpeechEvent, SpeechEventType, SpeechData

logging.basicConfig(level=logging.DEBUG)


@dataclass
class FakeAgent:
    # minimal agent placeholder required by AgentActivity construction
    _activity: object | None = None


class FakeSpeechHandle:
    def __init__(self):
        self.interrupted = False


async def simulate():
    # create a minimal AgentSession with default options (we only need _opts)
    session = AgentSession()

    agent = FakeAgent()
    activity = AgentActivity(agent, session)

    # attach a fake current speech to simulate "agent speaking"
    fake_speech = FakeSpeechHandle()
    activity._current_speech = fake_speech

    # filler-only interim transcript (low confidence) -> should be ignored
    ev1 = SpeechEvent(
        type=SpeechEventType.INTERIM_TRANSCRIPT,
        alternatives=[SpeechData(language="en", text="uh umm", confidence=0.2)],
    )

    activity.on_interim_transcript(ev1, speaking=True)

    # mixed filler + command (should not be ignored)
    ev2 = SpeechEvent(
        type=SpeechEventType.INTERIM_TRANSCRIPT,
        alternatives=[SpeechData(language="en", text="umm stop", confidence=0.3)],
    )

    activity.on_interim_transcript(ev2, speaking=True)

    # filler-only but high confidence -> should be treated as valid
    ev3 = SpeechEvent(
        type=SpeechEventType.FINAL_TRANSCRIPT,
        alternatives=[SpeechData(language="en", text="hmm", confidence=0.95)],
    )

    activity.on_final_transcript(ev3)

    # agent quiet: filler should be processed
    activity._current_speech = None
    ev4 = SpeechEvent(
        type=SpeechEventType.FINAL_TRANSCRIPT,
        alternatives=[SpeechData(language="en", text="umm", confidence=0.1)],
    )
    activity.on_final_transcript(ev4)

    print("Simulation done.")


if __name__ == "__main__":
    asyncio.run(simulate())
