
---
title: ''
summary: Academic portfolio of Xufan Gao, a doctoral researcher in computational biophysics at Zhejiang University.
type: landing

sections:
  - block: resume-biography-3
    content:
      username: me
      button:
        text: Download Academic CV
        url: uploads/Xufan-Gao-CV.pdf
    design:
      background:
        gradient_mesh:
          enable: true
      name:
        size: md
      avatar:
        size: medium
        shape: circle

  - block: markdown
    id: research
    content:
      title: Research
      text: |-
        I study how molecules bind, move, and assemble. My work combines all-atom and coarse-grained molecular dynamics with enhanced sampling, free-energy calculations, and machine learning. I also develop software for reproducible simulation setup and molecular featurization.

        I am interested in visiting doctoral research and joint training abroad, postdoctoral research after graduation, and R&D roles in computational chemistry, molecular modeling, and scientific software.
    design:
      columns: '1'

  - block: collection
    id: software
    content:
      title: Selected Software
      filters:
        folders:
          - projects
        featured_only: true
      sort_by: Weight
      order: asc
    design:
      view: article-grid
      columns: 3
      show_date: false
      show_read_time: false

  - block: collection
    id: papers
    content:
      title: Selected Journal Articles
      filters:
        folders:
          - publications
        featured_only: true
    design:
      view: citation

  - block: markdown
    id: contact
    content:
      title: Contact
      text: |-
        Zhejiang University · Hangzhou, China

        For research opportunities or collaboration, email [gxf1212@zju.edu.cn](mailto:gxf1212@zju.edu.cn).
    design:
      columns: '1'
---
