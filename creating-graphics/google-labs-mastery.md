# Google Labs AI Tools Deep Dive

## ImageFX Advanced Techniques

### Prompt Structure Formula

```
[Subject] + [Medium/Style] + [Artist/Aesthetic Reference] + [Lighting] +
[Color Palette] + [Composition] + [Quality Modifiers]
```

### Style Keywords That Work

**Art Styles**:
- digital art, digital painting
- oil painting, watercolor, acrylic
- vector art, flat design
- 3D render, CGI, Blender
- pencil sketch, charcoal drawing
- anime, manga style
- pixel art, 8-bit
- collage, mixed media
- art deco, art nouveau
- pop art, surrealism

**Photography Styles**:
- photorealistic, hyperrealistic
- portrait photography
- product photography
- street photography
- macro photography
- aerial/drone photography
- long exposure
- bokeh, shallow depth of field
- film grain, vintage film

**Lighting Keywords**:
- golden hour, blue hour
- studio lighting, softbox
- dramatic lighting, chiaroscuro
- rim lighting, backlit
- neon lighting, cyberpunk
- natural light, overcast
- hard shadows, soft shadows
- volumetric lighting, god rays

**Quality Boosters**:
- highly detailed
- 4K, 8K, ultra HD
- sharp focus
- professional quality
- award-winning
- trending on artstation
- masterpiece

### Prompt Templates by Use Case

**Logo Generation**:
```
"[Company name] logo, [industry] company, minimalist design,
[primary color] and [accent color], vector style, clean lines,
modern professional look, suitable for business card and website,
negative space design, memorable silhouette"
```

**Product Photography**:
```
"[Product] on [surface], studio product photography,
[lighting type] lighting, [background color] background,
commercial advertising style, high-end look, sharp details,
professional product shot, ecommerce ready"
```

**Social Media Graphics**:
```
"[Subject/theme] illustration, [style] art style,
vibrant [color scheme], perfect for social media,
eye-catching, modern design, [mood/emotion],
Instagram-worthy, shareable content"
```

**Hero Images/Banners**:
```
"[Scene/concept] wide shot, cinematic composition,
[lighting], [color grading], website hero image,
professional marketing material, high resolution,
[industry] business aesthetic, aspirational imagery"
```

**Icons/UI Elements**:
```
"[Object] icon, flat design, [color] color scheme,
minimal style, UI/UX design, app icon aesthetic,
clean vector graphics, consistent line weight,
modern interface design"
```

### Negative Prompts (What to Avoid)

When results include unwanted elements, try adding to your prompt:
- "no text, no watermark, no signature"
- "clean background, no clutter"
- "no distortion, proper proportions"
- "professional quality, no artifacts"

### Iterating on Results

1. **Like what you see but need tweaks?**
   - Keep core descriptors, modify specific elements
   - Add more specific style references
   - Adjust lighting/color descriptors

2. **Results too generic?**
   - Add unique style references
   - Be more specific about composition
   - Include emotional/mood descriptors

3. **Wrong style entirely?**
   - Start fresh with different medium keywords
   - Reference specific art movements or artists
   - Change the quality/rendering keywords

## MusicFX Mastery

### Prompt Structure

```
[Genre] + [Mood] + [Tempo] + [Instruments] + [Use Case]
```

### Example Prompts

**Corporate/Business**:
```
"uplifting corporate music, positive and professional,
medium tempo, piano and soft synths, perfect for
business presentation background"
```

**Tech/Startup**:
```
"modern electronic music, innovative and energetic,
upbeat tempo, synthesizers and digital beats,
tech company promotional video"
```

**Calm/Meditation**:
```
"ambient relaxation music, peaceful and serene,
slow tempo, soft pads and nature sounds,
meditation app background"
```

**Action/Energy**:
```
"driving rock music, powerful and motivating,
fast tempo, electric guitars and drums,
sports highlight reel"
```

## VideoFX Techniques

### Best Use Cases
- Short social media clips (5-15 seconds)
- Animated backgrounds
- Product reveals
- Conceptual visualizations
- Mood pieces

### Prompt Tips
- Describe the motion, not just the scene
- Specify camera movement (pan, zoom, static)
- Include timing cues
- Reference video styles (cinematic, documentary, etc.)

## Whisk Creative Combinations

### Style Transfer Workflow
1. Upload base image (your subject)
2. Upload style reference (art style you want)
3. Adjust blend settings
4. Generate remix

### Creative Applications
- Apply brand colors to stock photos
- Create consistent visual style across varied content
- Generate variations of a concept
- Artistic interpretations of products

## Integration Workflow

### ImageFX → Canva Pipeline

1. **Generate in ImageFX**
   - Create base imagery with detailed prompts
   - Download multiple variations
   - Save high-resolution versions

2. **Enhance in Canva**
   - Upload to Canva
   - Use Background Remover if needed
   - Apply filters/adjustments
   - Add text overlays
   - Incorporate into templates
   - Add brand elements

3. **Export Final**
   - Choose appropriate format
   - Set correct dimensions
   - Download for deployment

### Batch Generation Strategy

When creating multiple assets:
1. Establish core prompt structure
2. Create variations by modifying key elements
3. Generate batches with similar styling
4. Maintain visual consistency across set

## Troubleshooting

### Common ImageFX Issues

**"Results don't match prompt"**
- Be more specific with style keywords
- Try different medium descriptors
- Add quality modifiers
- Reduce prompt complexity

**"Faces/hands look wrong"**
- Add "proper proportions, anatomically correct"
- Try different angles/compositions
- Use artistic styles that are more forgiving

**"Colors are off"**
- Specify exact colors: "deep navy blue", "bright coral orange"
- Reference color palettes: "earth tones", "pastel colors"
- Include lighting that supports your color goals

**"Too busy/cluttered"**
- Add "minimalist", "clean", "simple composition"
- Specify "negative space", "uncluttered"
- Reduce number of elements in prompt

### Getting Consistent Results

For brand consistency across multiple generations:
1. Save successful prompts as templates
2. Use consistent style keywords
3. Specify exact colors when possible
4. Maintain similar composition language
5. Create a prompt style guide for the project
