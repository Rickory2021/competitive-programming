# competitive-programming

Personal competitive programming workspace — Python (PyPy 3-64 on Codeforces).

## Setup

```bash
make setup                    # create venv, install dev tools
source .venv/bin/activate
```

Install VS Code extensions:
- **Competitive Companion** (browser) — parses test cases from problem pages
- **Competitive Programming Helper** (VS Code, by Divyanshu Agrawal) — runs/judges solutions
- **Ruff** (VS Code, by Charlie Marsh) — linting/formatting

Verify the template path in `.vscode/settings.json` points to your actual absolute path for `templates/template.py`.

## Workflow

1. Open this folder in VS Code
2. Navigate to a problem in your browser (Codeforces, CSES, AtCoder, etc.)
3. Click the **Competitive Companion** green (+) icon
4. CPH creates a `.py` with your template pre-loaded and test cases ready
5. Write your solution, press **Ctrl+Alt+B** to run against all samples
6. Submit as **PyPy 3-64** on Codeforces
7. Run `make tidy` to organize solved files into `contests/<group>/`

## Hackpack

The `hackpack/` folder contains copy-paste reference implementations for contests. Open the relevant file and grab what you need — every snippet is self-contained.

## Submission Checklist

- [ ] Submit as **PyPy 3-64** (not CPython)
- [ ] `sys.stdin.readline` for fast I/O
- [ ] `sys.setrecursionlimit(300000)` if recursive (or convert to iterative)
- [ ] Correct MOD: `10**9+7` vs `998244353`
- [ ] Remove debug prints

## Supported Platforms

This workspace works with any judge supported by Competitive Companion (170+). The ones worth your time:

**Primary training**
- [Codeforces](https://codeforces.com) — largest community, regular contests, rating system
- [CSES](https://cses.fi) — best structured problem set, organized by topic
- [AtCoder](https://atcoder.jp) — excellent problem quality, strong on math/DP

**Interview prep**
- [HackerRank](https://hackerrank.com) — company assessments often use this

**Other solid judges**
- [Kattis](https://open.kattis.com) — university competitions, CPH has direct submit
- [CodeChef](https://codechef.com) — regular contests, good long challenges
- [DMOJ](https://dmoj.ca) — Canadian judge, clean interface

Full list of 170+ supported judges: [github.com/jmerle/competitive-companion](https://github.com/jmerle/competitive-companion)

**Not supported** (function-signature format, not stdin/stdout): LeetCode, GeeksforGeeks, InterviewBit, TopCoder. These require a different workflow — use their built-in editors or a dedicated extension like [leetcode-companion](https://marketplace.visualstudio.com/items?itemName=g4mbl3r.leetcode-companion).

The template's `stdin`/`stdout` + multi-test-case loop covers all supported platforms. Delete the `T` loop for single-test judges like CSES.

## Resources

| Resource | URL |
|----------|-----|
| CSES Problem Set | https://cses.fi/problemset |
| cp-algorithms | https://cp-algorithms.com |
| CF Problemset | https://codeforces.com/problemset |
| CF EDU | https://codeforces.com/edu/courses |