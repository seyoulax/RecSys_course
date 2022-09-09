# RecSys course
The course on recommender systems conducted in National Research University - Higher School of Economics (Moscow, Russia). Academic year 2022-2023. 

Course on recommender systems.

Week1
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
- Basic baseline (TopPopular)
- Item-based and user-based similarity, similarity metrics. 
- Matrix Factorization (SVD et al.)
- EASE

Week2
-----
Seminar 3
- Collaborative Filtering (ALS and iALS, HALS, NeuralCF) 
- implicit library

Seminar 4
- Content-based recommender models
- DSSM for RecSys
- Hybrid recommenders taxonomy
- LightFM (hybrid content model), Lightfm library

Week3
-----
Seminar 5
- Gradient boosting for ranking task
- Example of cascade recommender model (using gradient boosting on the second level)
- Important preprocessing steps
- Cross-validation types

Seminar 6
- Autoencoders and Variational autoencoders for RecSys (VAE, Mult-VAE, Multi-VAE, Rec-VAE)

Week 4
------
Seminar 7
- Sequential и session-based models
- RecBole library
- Next-basket and next-item prediction tasks

Seminar 8
- Transformer-based models for RecSys (BERT4Rec, SASRec, etc.)
- Transformers4rec NVIDIA library

Week 5
--------
Seminar 9
- Context-aware recommender models
- Time-aware и time-dependent models
- Geo-dependent models

Seminar 10
- Graph-based recommender systems overview
- Inductive learning (out-of-sample users, cold start problem)
- LightGCN, GF-CF, P3 alpha, GraphSage -> PinSage

Week 6
-----
Seminar 11
- Knowledge-based graph recommender systems overview
- KDA, KGAT, KGCN, RippleNet

Seminar 12
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
