# Gautam Yadav — Portfolio

A static portfolio focused on learning design and impact, with four case studies, research, and a printable résumé. No framework, package installation, or build step is required.

## Preview

```sh
python3 -m http.server 8775 --bind 127.0.0.1
```

Open <http://127.0.0.1:8775/>. Run `python3 scripts/check-site.py` to check the updated pages' local links and fragments.

## Editing

- `index.html`: introduction, selected work, research, experience, and contact information.
- `work/author-your-first-skill.html`, `work/learnlab.html`, `projects/equation.html`, and `projects/CTAT.html`: the four selected case studies. Their existing URLs are preserved. The standalone assessment example remains available at its original URL but is not listed in the current visitor journey.
- `resume.html`: readable résumé with a browser Print / Save PDF button.
- `css/portfolio.css` and `js/portfolio.js`: shared presentation and the small print/year enhancements. Content and navigation work without JavaScript.

The previous homepage is preserved in `portfolio-2020.html`. The original Algebra and CTAT pages are preserved as `old_portfolio/equation-2020.html` and `old_portfolio/CTAT-2020.html`. The current case-study URLs use the shared design system; other historical pages and assets remain intact. No archive link appears in the current portfolio.

## Sources and content choices

Checked September 12, 2026:

- The seven recent résumé documents supplied on September 12, 2026, supersede the older résumé for experience dates and current emphasis. They establish the Learning Engineer start as September 2020 and the Learning Engineering Research Assistant period as May–August 2020. The connected Drive “Work Samples - Gautam Yadav” document also informed project descriptions. No source documents or credentials were copied into public assets, and private Drive links are not used as portfolio calls to action.
- [LearnLab instructor profile](https://learnlab.org/certificate/courses/using-generative-ai-to-develop-active-learning-experiences/) supports the current role, course context, and profile photo. The photo is stored locally under `assets/portfolio/`.
- [Author Your First Skill](https://gautamyadavs.github.io/author-your-first-skill/) supports the description of role selection, authoring decisions, exercises, and feedback. The live course version requires an email to record progress; this is stated beside its link. The earlier prototype URL in the Work Samples document returned 404 and is not linked.
- [MCQ Quality repository](https://github.com/gautamyadavs/mcq-quality) supports the 19-criterion rubric, shared validator, skill, MCP server, and workflow descriptions. The custom GPT is linked separately and may require a ChatGPT account.
- [Beyond Repetition](https://arxiv.org/abs/2405.09655) supports the research description and authors. Study sample counts are not featured in the current portfolio.
- [David Hou's portfolio](https://davidhou17.github.io/) informed the personal introduction, concise project presentation, and direct contact links. His copy and assets are not reused.

The web résumé synthesizes the supplied résumé variants around learning design and impact. No source DOCX files are published. The conflicting 29/31 course count is omitted. Program scale and mastery estimates come from the supplied résumés, with mastery described as an estimate across offerings. The GenAI feedback study is described as finding no statistically significant difference, not equivalence. The broader agentic content-production project is not presented as completed work.

## Publication

This version targets the existing GitHub Pages root at `gautamyadavs.github.io`. No hosting migration or backend is needed. Deploy from the `master` branch and repository root once GitHub Pages is enabled. On September 13, 2026, Pages settings required either making this private repository public or upgrading the account before further deployments.

The local workspace began as an empty Git repository without a remote. The old public site files were restored and compared with the connected repository's blob hashes: all 177 preserved files matched. The original homepage is archived separately. Updates are applied on top of the existing repository history; do not replace that history with the empty local history.

## Shared design system

`css/portfolio.css` defines one sans-serif family with regular and bold weights, a shared type scale, white and neutral surfaces, one blue action color, a 1,100px container, 24px gutters, and spacing based on 8px. Homepage project entries use the same hierarchy; all four case studies share section navigation, role/audience/context facts, readable text widths, artifact captions, and full-size image links. Mobile layouts keep all primary navigation visible. Core content and links are static HTML; JavaScript only updates the year and enables printing.

The lesson anatomy SVG was extracted from the public lesson and includes its source hotspot styling, with annotations shown as a static reference. The LearnLab catalog image is a screenshot of the public catalog. The Algebra and CTAT illustrations are original project artifacts. Their colors and proportions are preserved; they are not portfolio UI themes.

## Validation of the redesign

Checked September 12, 2026:

- Local links, fragment targets, one main heading per page, and image descriptions pass for all seven checked pages.
- Homepage layout checked at 320, 390, 768, and 1440 CSS pixels; all four selected case studies and the résumé checked at 390 pixels without horizontal overflow. Artifact views were also inspected at desktop and tablet sizes.
- At 200% root text size, the homepage retained its content and navigation without horizontal overflow.
- A temporary local server with `script-src 'none'` confirmed that project navigation and résumé content work without scripts; the print button remains hidden when its enhancement cannot run.
- Keyboard Tab exposes the skip link and a visible focus outline; Enter moves focus to the main content. Contact remains accessible from mobile navigation.
- Shared text and action colors exceed 4.5:1 against both page surfaces. Motion is limited to native smooth scrolling, which is disabled for reduced-motion preferences.
- Primary demo, repository, and research links returned HTTP 200, including the algebra tutor and CTAT repository.
- The print button was invoked successfully. Native print-dialog inspection was unavailable in Codex, so final printed pagination still needs a manual browser check.
