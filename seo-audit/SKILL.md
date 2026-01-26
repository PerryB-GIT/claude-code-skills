---
name: seo-audit
description: Comprehensive SEO audit checklist for client websites. Covers technical SEO, on-page optimization, local SEO, Core Web Vitals, and generates actionable reports.
version: 1.0.0
author: Perry
---

# SEO Audit Skill

You are an SEO specialist helping Perry audit client websites for search engine optimization issues and opportunities.

## Quick Audit Commands

```bash
# Lighthouse audit (performance, SEO, accessibility)
npx lighthouse https://example.com --output html --output-path ./audit.html

# Check robots.txt
curl -s https://example.com/robots.txt

# Check sitemap
curl -s https://example.com/sitemap.xml | head -50

# Check page speed
curl -o /dev/null -s -w 'Time: %{time_total}s\n' https://example.com
```

## Technical SEO Checklist

### Crawlability & Indexing

```markdown
## Crawlability
- [ ] robots.txt exists and is properly configured
- [ ] XML sitemap exists and is submitted to Google Search Console
- [ ] No important pages blocked by robots.txt
- [ ] No excessive use of noindex tags
- [ ] Sitemap includes all important pages
- [ ] Sitemap excludes thin/duplicate content

## Indexing
- [ ] Site is indexed in Google (site:domain.com)
- [ ] Important pages appear in search results
- [ ] No index bloat (too many low-value pages indexed)
- [ ] Canonical tags properly implemented
- [ ] No duplicate content issues
```

### Site Architecture

```markdown
## URL Structure
- [ ] URLs are clean and descriptive (/services/web-design vs /page?id=123)
- [ ] URLs use hyphens, not underscores
- [ ] No excessive URL parameters
- [ ] Consistent trailing slash usage
- [ ] HTTPS enforced (redirects from HTTP)

## Internal Linking
- [ ] Logical site hierarchy (3 clicks to any page)
- [ ] Breadcrumbs implemented
- [ ] Important pages linked from homepage
- [ ] No orphan pages (pages with no internal links)
- [ ] No broken internal links
```

### Mobile & Performance

```markdown
## Mobile-Friendliness
- [ ] Responsive design (passes Google Mobile-Friendly Test)
- [ ] No horizontal scrolling on mobile
- [ ] Tap targets properly sized (48px minimum)
- [ ] Text readable without zooming
- [ ] No intrusive interstitials

## Core Web Vitals
- [ ] LCP (Largest Contentful Paint) < 2.5s
- [ ] FID (First Input Delay) < 100ms
- [ ] CLS (Cumulative Layout Shift) < 0.1
- [ ] TTFB (Time to First Byte) < 800ms

## Performance
- [ ] Images optimized (WebP, lazy loading)
- [ ] CSS/JS minified
- [ ] Gzip/Brotli compression enabled
- [ ] Browser caching configured
- [ ] CDN implemented
```

### Security & Technical

```markdown
## Security
- [ ] SSL certificate valid and not expiring soon
- [ ] HSTS header implemented
- [ ] No mixed content warnings
- [ ] Security headers configured (CSP, X-Frame-Options, etc.)

## Technical
- [ ] 404 page exists and is helpful
- [ ] No redirect chains (max 1 redirect)
- [ ] No redirect loops
- [ ] Server response codes correct (200, 301, 404)
- [ ] Structured data validates without errors
```

## On-Page SEO Checklist

### Meta Tags

```markdown
## Title Tags
- [ ] Every page has a unique title
- [ ] Titles are 50-60 characters
- [ ] Primary keyword near the beginning
- [ ] Brand name at end (if space allows)
- [ ] Compelling and click-worthy

## Meta Descriptions
- [ ] Every page has a unique meta description
- [ ] Descriptions are 150-160 characters
- [ ] Include primary keyword naturally
- [ ] Include call-to-action
- [ ] Accurately describe page content

## Other Meta Tags
- [ ] Viewport meta tag present
- [ ] Open Graph tags for social sharing
- [ ] Twitter Card tags
- [ ] Canonical URL specified
- [ ] Language/hreflang tags (if multilingual)
```

### Content Optimization

```markdown
## Headings
- [ ] One H1 per page (includes primary keyword)
- [ ] Logical heading hierarchy (H1 → H2 → H3)
- [ ] Headings are descriptive and useful
- [ ] No skipped heading levels

## Content Quality
- [ ] Unique, valuable content on each page
- [ ] Minimum 300+ words on important pages
- [ ] Keywords used naturally throughout
- [ ] Content answers user search intent
- [ ] No keyword stuffing
- [ ] Content is scannable (bullets, short paragraphs)

## Images
- [ ] All images have descriptive alt text
- [ ] Alt text includes keywords where natural
- [ ] Image file names are descriptive
- [ ] Images are appropriately sized
- [ ] No missing images (broken image links)
```

## Local SEO Checklist

```markdown
## Google Business Profile
- [ ] GBP claimed and verified
- [ ] NAP (Name, Address, Phone) consistent everywhere
- [ ] Business hours accurate
- [ ] Categories properly selected
- [ ] Photos uploaded and recent
- [ ] Reviews being collected and responded to
- [ ] Posts published regularly

## Local Signals
- [ ] Local schema markup implemented
- [ ] NAP in footer or contact page
- [ ] Embedded Google Map on contact page
- [ ] Local keywords in content
- [ ] City/region in title tags (where appropriate)
- [ ] Listed in relevant local directories

## Citations
- [ ] Yelp listing accurate
- [ ] Facebook page consistent
- [ ] Apple Maps listing
- [ ] Bing Places listing
- [ ] Industry-specific directories
```

## Structured Data

```markdown
## Schema Markup to Consider
- [ ] Organization/LocalBusiness schema
- [ ] Breadcrumb schema
- [ ] FAQ schema (if applicable)
- [ ] Review/Rating schema
- [ ] Product schema (e-commerce)
- [ ] Article schema (blog posts)
- [ ] Service schema

## Validation
- [ ] Test with Google Rich Results Test
- [ ] Test with Schema.org validator
- [ ] No errors or warnings
```

## SEO Audit Report Template

```markdown
# SEO Audit Report: [Website]
**Audit Date**: [Date]
**Prepared By**: {YOUR_NAME}

## Executive Summary

**Overall SEO Health**: [Poor/Fair/Good/Excellent]

### Key Findings
- 🔴 Critical Issues: [X]
- 🟡 Warnings: [X]
- 🟢 Passed: [X]

### Top 3 Priority Fixes
1. [Issue 1] - Impact: High
2. [Issue 2] - Impact: High
3. [Issue 3] - Impact: Medium

---

## Technical SEO: [Score/100]

### Critical Issues 🔴
| Issue | Impact | Fix |
|-------|--------|-----|
| [Issue] | [Description] | [Solution] |

### Warnings 🟡
| Issue | Impact | Fix |
|-------|--------|-----|
| [Issue] | [Description] | [Solution] |

### Passed ✅
- [Item 1]
- [Item 2]

---

## On-Page SEO: [Score/100]

### Pages Analyzed
| Page | Title | Meta Desc | H1 | Issues |
|------|-------|-----------|-----|--------|
| Homepage | ✅ | ⚠️ | ✅ | Meta desc too short |
| About | ✅ | ✅ | ❌ | Missing H1 |

### Content Recommendations
- [Page]: [Recommendation]

---

## Local SEO: [Score/100]

### Google Business Profile
- Status: [Claimed/Unclaimed]
- Reviews: [X] reviews, [X.X] average
- Last Post: [Date]

### NAP Consistency
| Platform | Consistent? | Notes |
|----------|-------------|-------|
| Website | ✅ | - |
| GBP | ⚠️ | Phone format different |
| Yelp | ❌ | Old address |

---

## Performance: [Score/100]

### Core Web Vitals
| Metric | Mobile | Desktop | Target |
|--------|--------|---------|--------|
| LCP | [X]s | [X]s | < 2.5s |
| FID | [X]ms | [X]ms | < 100ms |
| CLS | [X] | [X] | < 0.1 |

### Recommendations
1. [Optimization 1]
2. [Optimization 2]

---

## Action Plan

### Immediate (This Week)
- [ ] [Task 1]
- [ ] [Task 2]

### Short-term (This Month)
- [ ] [Task 3]
- [ ] [Task 4]

### Ongoing
- [ ] [Task 5]
- [ ] [Task 6]

---

## Tools Used
- Google Lighthouse
- Google Search Console
- Google PageSpeed Insights
- Schema Validator
- Screaming Frog (if applicable)
```

## Quick Reference: Meta Tag Templates

```html
<!-- Basic SEO Meta Tags -->
<title>Primary Keyword - Secondary Keyword | Brand Name</title>
<meta name="description" content="Compelling 150-160 char description with keyword and CTA.">
<link rel="canonical" href="https://example.com/page/">

<!-- Open Graph -->
<meta property="og:title" content="Page Title">
<meta property="og:description" content="Description for social sharing">
<meta property="og:image" content="https://example.com/image.jpg">
<meta property="og:url" content="https://example.com/page/">
<meta property="og:type" content="website">

<!-- Twitter -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Page Title">
<meta name="twitter:description" content="Description">
<meta name="twitter:image" content="https://example.com/image.jpg">

<!-- Local Business Schema -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Business Name",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "123 Main St",
    "addressLocality": "City",
    "addressRegion": "State",
    "postalCode": "12345"
  },
  "telephone": "+1-555-555-5555",
  "url": "https://example.com"
}
</script>
```
