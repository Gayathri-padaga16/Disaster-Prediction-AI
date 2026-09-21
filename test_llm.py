from llm.explain_risk import explain_flood_risk

print("🔍 Testing Gemini LLM...\n")

response = explain_flood_risk("High")

print("✅ Gemini Response:\n")
print(response)
