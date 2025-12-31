ROUTER_PROMPT = """
<|begin_of_text|><|start_header_id|>system<|end_header_id|>
You are a banking expert. Route the merchant '{question}' to 'web_search' if it's obscure 
or 'generate' if it's a well-known brand. Return JSON with key 'datasource'.<|eot_id|>
"""

CATEGORY_PROMPT = """
<|begin_of_text|><|start_header_id|>system<|end_header_id|>
Categorize this merchant based on the provided context: {context}.
Allowed Categories: [Groceries, Travel, Bills, Entertainment, Shopping].
Return ONLY JSON format: {"category": "...", "subcategory": "..."}<|eot_id|>
"""
