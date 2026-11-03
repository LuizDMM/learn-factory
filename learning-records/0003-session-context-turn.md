# Session fills the box; a turn ends when the agent yields

Luiz classified all four setups on the first pass: this thread = session, the grill = turn, one API payload = context window, one tool round-trip = provider request.

Turn: first wording was “user message to the model’s response.” He meant the response that *ends* the turn, not the first API hit; he picked “yields back to you” on the follow-up.

Context window took two rewrites. First: “what the model has access during a session / everything it knows” (session + parametric knowledge). Second: “history of everything that happened in a session” (the session again). After a forced pick, he wrote the prefix from system prompt to the current request.

**Implications:** 0004 can move to smart zone / dumb zone. Do not call the window memory. Do not treat session history as the same object as the window (compaction exists). Do not start a second task in this teaching thread to “save a session.”
