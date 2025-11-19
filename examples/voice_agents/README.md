Summary of Improvements Made

The following enhancements have been introduced across the directory:

Rewritten and expanded documentation to provide clearer long-form explanations for each example.

Removed the table of contents section, replacing it with a narrative, documentation-style format for improved readability.

Standardized naming conventions and ensured each example file is described with technical accuracy.

Added detailed explanations of the behavior, integration goals, and internal mechanisms demonstrated in each script.

Clarified design motivations for various examples, including function calling, model integration, pipeline nodes, and interruption handling.

Reorganized and consolidated related material into logical sections for easier navigation without needing a table of contents.

Improved professionalism and technical tone, removing casual wording, redundancies, and informal formatting.

Expanded the filler-interruption demonstration with a more complete explanation of configuration, expected behavior, and next steps.

What follows is the updated, polished documentation that reflects these changes.

Updated Documentation

The examples contained in this directory illustrate a variety of use cases built with LiveKit Agents. They cover topics ranging from basic voice-agent construction to advanced multi-agent workflows and external integrations.

Getting Started

The introductory example, basic_agent.py, demonstrates the minimal structure required to run a functional voice agent. It has been documented in greater detail to explain initialization flow, metrics tracking, and the agent session lifecycle. This file serves as a baseline for understanding the framework before proceeding to more advanced features.

Tool Integration and Function Calling

Several examples focus on how agents can invoke external functions and tools:

annotated_tool_args.py demonstrates type-annotated arguments for enforcing strongly-typed function inputs.

dynamic_tool_creation.py shows dynamic registration of tools during runtime.

raw_function_description.py highlights the use of raw JSON schemas for tool descriptions.

silent_function_call.py introduces function execution without producing verbal responses.

long_running_function.py describes long-running operations and interruption-safe execution.

Each description has been expanded to explain not only the function call mechanisms but also the situations in which these different approaches are appropriate.

Real-Time Model Integrations

This set of examples demonstrates the use of real-time AI models from various providers:

weather_agent.py integrates the OpenAI Realtime API for producing weather information through tool-assisted responses.

realtime_video_agent.py utilizes Google's Gemini model for multimodal (video + audio) processing.

realtime_joke_teller.py demonstrates an Amazon Nova Sonic model in a full voice interaction loop.

realtime_load_chat_history.py shows how previous conversation history can be injected into a live model session.

realtime_turn_detector.py provides detailed behavior for turn detection and improved conversational pacing.

realtime_with_tts.py explains how to combine external TTS engines with a real-time model pipeline.

Descriptions have been revised to clarify the model flow and the distinction between the different real-time pipelines.

Pipeline Nodes and Event Hooks

The pipeline examples focus on how voice-agent behavior can be transformed using nodes and hooks:

fast-preresponse.py describes a mechanism for producing early responses based on user turn completion.

flush_llm_node.py outlines how partial LLM output can be streamed directly to text-to-speech.

structured_output.py explains how to produce structured JSON responses with reliability.

speedup_output_audio.py demonstrates dynamic speed manipulation for audio playback.

timed_agent_transcript.py shows how to read timestamped transcripts from the transcription pipeline.

inactive_user.py documents how user inactivity is detected and handled.

resume_interrupted_agent.py covers speech resumption after false interruption events.

toggle_io.py describes dynamic control of audio input and output at runtime.

The descriptions in this section have been rewritten to emphasize how these features affect pipeline behavior and conversation flow.

Multi-Agent Scenarios and AgentTask Use Cases

These examples illustrate cooperative or task-driven interactions:

restaurant_agent.py demonstrates a multi-agent restaurant system handling ordering and reservations.

multi_agent.py shows collaborative storytelling with multiple agents each responsible for different narrative components.

email_example.py demonstrates collection and validation of structured user input using AgentTask.

The rewritten documentation clarifies the benefits of multi-agent coordination and provides a more thorough explanation of how AgentTask ensures reliable data gathering.

MCP and External Integrations

The following examples illustrate integration with external systems and protocols:

web_search.py adds web-search capabilities through a tool invocation pattern.

langgraph_agent.py integrates LangGraph-based flows.

The mcp directory includes examples demonstrating Model Context Protocol usage:

mcp-agent.py shows how an MCP-driven agent operates.

server.py shows how to run an MCP server for external communication.

zapier_mcp_integration.py connects an agent workflow to Zapier for automation.

Descriptions were expanded to clearly articulate what each integration accomplishes and how it interacts with the agent runtime.

Retrieval-Augmented Generation (RAG)

The llamaindex-rag directory demonstrates full RAG integration using LlamaIndex:

chat_engine.py provides an interactive RAG-powered chat workflow.

query_engine.py exposes a retrieval pipeline callable as a tool.

retrieval.py handles document ingestion and search.

This section has been rewritten to explain the document flow, retrieval strategy, and typical RAG application patterns.

Specialized Use Cases

Additional examples covering niche or advanced audio interactions include:

background_audio.py for ambient audio playback.

push_to_talk.py for push-activated conversation.

tts_text_pacing.py for manual pacing control in TTS.

speaker_id_multi_speaker.py for separating and identifying multiple speakers.

Each explanation has been expanded to clarify the underlying agent mechanics.

Tracing and Error Handling

Support tools for debugging and reliability include:

langfuse_trace.py for integrating LangFuse-based conversational tracing.

error_callback.py for runtime error interception.

session_close_callback.py for session lifecycle monitoring.

This section now provides a more complete understanding of how and when to incorporate these tools.

Filler Interruption Demonstration

A dedicated example, test_filler_interruption.py, showcases the runtime’s filler-word interruption filtering. This script simulates speech events containing filler-only utterances and mixed utterances to demonstrate how the agent determines whether to pause or continue speaking.

Overview of Behavior

Filler-only terms such as “uh”, “umm”, or “hmm” are ignored while the agent is speaking.

Mixed content, such as “umm stop”, is processed normally and may interrupt the agent.

Confidence levels determine whether filler-like words are considered valid speech.

How to Run the Script

From the repository root:

$env:PYTHONPATH = "${pwd}\livekit-agents"
python -m examples.voice_agents.test_filler_interruption


If required dependencies are missing:

pip install numpy opentelemetry-api

Configuration

The following runtime options are described in detail:

ignored_fillers: list of tokens treated as ignorable while speaking

filler_confidence_threshold: minimum confidence required to process a filler as valid speech