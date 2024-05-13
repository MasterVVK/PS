paragraphs = ["Абзац 1", "Абзац 2", "Абзац 3", "Абзац 4", "Абзац 5", "Абзац 6"]
for i, paragraph in enumerate(paragraphs[:3]):
    print(f"{i+1}. {paragraph}")


print(enumerate(paragraphs[:3]))

colors = ['red', 'green', 'blue', 'yellow']
for index, color in enumerate(colors, start=1):
    print(index, color)
