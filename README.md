# RecSys course
The course on recommender systems conducted in National Research University - Higher School of Economics (Moscow, Russia). Academic year 2022-2023 /
Курс по рекомендательным системам, который проводится в Национальном исследовательском университете Высшей школе Экономики (Москва). Академический год 2022 - 2023. 


## Полезные материалы

- [Wiki-страница курса,](http://wiki.cs.hse.ru/RecSys_2022_2023) на ней для каждого семинара публикуются дополнительные материалы, которые необходимо просмотреть на неделе, когда проходит семинар. 
- Материалы для каждого семинара лежат в папках `/seminar*`
- Если вы хотите скачать из репозитория конкретную папку, просто вставьте ссылку на неё [в сервис для скачки.](https://minhaskamal.github.io/DownGit/#/home)
- Любые вопросы можно задавать в чат с технической поддержкой[![TG1](https://img.shields.io/badge/Telegram-chat-blue)](https://t.me/+51dCYfNAXlZiMjYy)
-  [Таблица с вашими оценками](https://docs.google.com/spreadsheets/d/1RvuhuC1euQw0rSNANKWvG7wWSjiAiuWd/edit?usp=sharing&ouid=104963596150558587903&rtpof=true&sd=true)

## Самый важный раздел

Оценка ставится по формуле:

```
0.3 * Home Assignments + 0.15 * Article Summary + 0.15 * Weekly Quizzes + 0.4 * Exam
```
где
Home Assignments - 3 домашних работы в Jupyter Notebook (max 10 баллов за каждую). 
Article Summary - конспект/презентация статьи из предложенного списка с критическим анализом (без выступления на семинаре) (max 10 баллов). 
Weekly Quizzes - 7 квизов по мотивам материалов семинаров, которые сдаются перед началом следующего занятия в Google Forms (ариф.среднее за все квизы, max 10 баллов за каждый). 
Exam - письменный экзамен в формате решения case-study построения рекомендательной системы для бизнеса (max 10 баллов). 


## Course Outline / Большой план маленьких побед

Week 1
-----

Seminar 1
- Examples of RecSys models in production.
- Formalization of the ranking (recommender systems) task (2 popular types of tasks, 2 types of data sets). 
- Ranking functions (BPR, WARP, RankNET, LambdaRank).
- Metrics for the quality estimation (Hitrate, Precision@k, Recall@k, MAP@k, NDCG@k).
- Taxonomy of RecSys approaches ([MF, FM, CF & other general], Content-based [including knowledge graph based, GB for ranking], Context-based, Sequential and session-based models, RL-based models, Hybrid [including two-level cascade]) approaches.
- Recommended sources on RecSys.

Seminar 2
- Hands-on example on the MovieLens dataset: movie recommender system. 
- Basic baselines

Week 2
-----
Seminar 3 - 4
- Item-based and user-based similarity, similarity metrics. 
- Matrix Factorization (SVD et al.)
- Collaborative Filtering (ALS and iALS, HALS, NeuralCF) 

Week 3
-----
Seminar 5
- Content-based recommender models
- DSSM for RecSys
- Hybrid recommenders taxonomy
- LightFM (hybrid content model), Lightfm library

Seminar 6
- Gradient boosting for ranking task
- Example of cascade recommender model (using gradient boosting on the second level)
- Important preprocessing steps
- Cross-validation types

Week 4
------
Seminar 7
- Sequential models
- Next-basket and next-item prediction tasks

Seminar 8
- Context-aware recommender systems
- Time-aware и time-dependent models

Week 5
--------
Seminars 9 - 10
- Autoencoders and Variational autoencoders for RecSys (VAE, Mult-VAE, Multi-VAE, Rec-VAE)

Week 6
-----
Seminar 11
- Graph-based recommender systems overview
- Inductive learning (out-of-sample users, cold start problem)
- LightGCN, GF-CF, P3 alpha, GraphSage -> PinSage
- Knowledge-based graph recommender systems overview
- KDA, KGAT, KGCN, RippleNet

Seminar 12

- Transformer-based models for RecSys (BERT4Rec, SASRec, etc.)
- Transformers4rec NVIDIA library
- RL for RecSys overview
- Hands-on example of RL model for recommender systems

Week 7
-----
Seminar 13
- Explainability & interpretability of recommender systems
- Attention is not explanation? 

Seminar 14
- Designing anf analyzing A/B tests in recommeder systems
- Feedback loop problem
- Bias types and debiasing techniques
- Multiarmed bandits
- RL testing 

Week 8
-----
Seminar 15 & Seminar 16
- Vanilla Production-ready RecSys service.


## Контрибьюторы и создатели

* [Ананьева Марина](https://github.com/anamarina)
* [Милоградский Саша](https://github.com/Nemexur)
* [Милоградский Саша](https://github.com/fotol1)
* [Рамазанова Ая](https://github.com/AyaRamazanova)


## Лицензия

Весь контент, созданный для этого курса распространяются на правах лицензии [MIT License](https://github.com/hse-econ-data-science/dap_2020_fall/blob/master/LICENSE) Материалы публикуются как общественное достояние.
