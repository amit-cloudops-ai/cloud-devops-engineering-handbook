# Tool Calling

A tool call is a request to invoke a predefined operation. Treat it as an untrusted proposal until the application validates the tool name, arguments, identity, target and authorization.

Record schema, required fields, allowed values, timeout, retry rules, idempotency, error responses and side effects for every tool. Use separate read and write tools. Never pass arbitrary shell execution to an agent with broad infrastructure credentials.
