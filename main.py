oneai.api_key = "ONE_AI_API_KEY" # api key
text = "YOUR_URL"

pipeline = oneai.Pipeline(
  steps = [
		oneai.skills.HtmlToArticle(),
		oneai.skills.Topics(),
		oneai.skills.Emotions(),
  ]
)

output = pipeline.run(text)