
# Xufan Gao · Academic Portfolio

English-language academic website for research collaborations, visiting doctoral and joint-training opportunities, postdoctoral applications, and computational research and development roles. The site uses HugoBlox and is configured for GitHub Pages.

[Academic website](https://gxf1212.github.io/academic-cv/) · [Google Scholar](https://scholar.google.com/citations?user=f8pi1BUAAAAJ) · [ORCID](https://orcid.org/0009-0004-0065-3172) · [Research Notes](https://gxf1212.github.io/notes/#/) · [Mendelevium](https://gxf1212.github.io/mendelevium/) · [Bilibili](https://space.bilibili.com/441196634)

## Local preview

Install Go, the extended Hugo version specified in [hugoblox.yaml](hugoblox.yaml), Node.js 22.13 or newer, and the pnpm version in [package.json](package.json). Then run

```sh
pnpm install --frozen-lockfile
pnpm dev
```

Run `pnpm build` to build the production site and its Pagefind index.

## 发布到 GitHub Pages

1. 打开仓库的 [Settings → Pages](https://github.com/gxf1212/academic-cv/settings/pages)，在 **Build and deployment → Source** 选择 **GitHub Actions**。
2. 推送 `main` 后，已有的 [部署工作流](.github/workflows/deploy.yml) 会构建并发布。也可在 [Actions](https://github.com/gxf1212/academic-cv/actions) 手动运行 **Deploy website to GitHub Pages**。
3. 部署成功后，访问 [公开站点](https://gxf1212.github.io/academic-cv/)。若使用 Google Search Console，可验证该 URL 前缀并提交 `/academic-cv/sitemap.xml`。

## Content maintenance

| Content | Location |
| --- | --- |
| Name, contact, affiliations, education and research appointments | [Author profile](data/authors/me.yaml) |
| Homepage and research interests | [Home](content/_index.md) |
| Technical skills, entrepreneurship and academic service | [Experience](content/experience.md) |
| Software and research portfolio | [Projects](content/projects/) |
| Journal articles, preprints and intellectual property | [Publications](content/publications/) |
| Conference presentations | [Presentations](content/events/) |
| Downloadable CV | [PDF](static/uploads/Xufan-Gao-CV.pdf) |

The source for the public CV is [cv/xufan-gao-cv.py](cv/xufan-gao-cv.py). To regenerate the download, install ReportLab and run `python cv/xufan-gao-cv.py` from the repository root.

### 成果状态

- 已正式发表的同行评审论文归入 **Peer-Reviewed Articles**，附出版记录和 DOI。
- 已公开的预印本归入 **Preprints**，沿用公开版本的作者顺序，附平台和 DOI。同期在审时可仅展示可查证的预印本状态。正式发表后更新为期刊条目，并保留需要的预印本链接。
- 未公开的在投、审稿中和准备中稿件优先放在申请专用 CV。若合作者同意公开，可新增独立的 **Manuscripts under review**，只填获准公开的题名、作者和当前状态。已正式接收的稿件可标为 **Accepted** 或 **In press**，等正式出版后补齐引文。
- 待确认的课题结论、内部稿件编号和未发布数据保留在项目资料中。此仓库的 Markdown、PDF 和提交历史均按可公开分享的材料整理。

## 待补资料

| 字段 | 占位 / 更新位置 |
| --- | --- |
| 预计答辩和毕业年月、正式学位全称及论文题目 | 待确认，见 [个人资料](data/authors/me.yaml) |
| 联培／访问可到岗时间、周期及资助方式 | 待确认，更新 [首页](content/_index.md) |
| 博后／研发岗位可到岗时间 | 待确认，更新 [首页](content/_index.md) |
| 英语考试分数和日期 | 待补，更新 [经历页](content/experience.md) |
| 推荐人和申请专用联系方式 | 待确认，可放入申请专用 CV |
| 奖项与资助、教学与指导、同行评审与学术服务 | 已有团队奖项和部分服务，待补可核实的项目、角色及年份，再评估是否开独立板块 |
| 在研论文、演讲和知识产权后续状态 | 待公开记录或确认后更新 [成果页](content/publications/) 和 [演讲页](content/events/) |
| FEbuilder 源码及在线服务 | 待填写可公开访问的入口，现有 [项目页](content/projects/febuilder/index.md) 提供归档海报 |
| 个人 LinkedIn 或其他职业主页 | 待补，更新 [个人资料](data/authors/me.yaml) |

资料以本地个人简历、论文和项目记录为基础。公开页面的论文元数据以出版机构或 DOI 注册记录为准。
