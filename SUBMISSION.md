# Submission Manifest — Project 2

Fill this in before submitting. The grading agent reads it first.

## Student
- Name (RIT ID): Srujan Vandavasi (sv9211)

## Course level
- [X] 520 (undergraduate)
- [ ] 620 (graduate)

## Dataset
UNSW_NB15_training-set.csv from the public mirror described in data/README.md
(not the Drive archive); SHA-256 checked against the checksum in data/README.md
[confirm you verified it]. Sample: 3,730 rows x 39 numeric features (id and label
dropped; categorical columns dropped by the numeric selector), class-balanced with
cap 4,000 (400 per class, 130 Worms). Labels were used only for sampling and
evaluation, never as clustering features.


## How to reproduce
```bash
make setup
# Download the course Drive archive and extract data/UNSW_NB15_training-set.csv
# See data/README.md; make data is an optional mirror fallback / checksum check.
make reproduce
```
Anything non-default the grader must know (data download, runtime):

## Your implementation
- Confirm `config.yaml` has `kmeans.implementation: scratch`: [X]
- Initialization used (`random` / `kmeans++`): random
- How you handle **empty clusters**:If a cluster ends an update step with no points, its centroid is re-seeded
- Convergence criterion and tolerance:Each restart stops when the maximum centroid shift is below tol (1e-4), or the
labels stop changing
- Agreement with the reference (each run’s `reference_check` in metrics.json; same geometry):
  - Euclidean `inertia_ratio` / `ari_vs_reference`:
  - Mahalanobis `inertia_ratio` / `ari_vs_reference`:

## Choosing k
- k you report, and the evidence (elbow / silhouette):
- If the best silhouette k differs from the number of true classes, explain:

k = 10, the highest silhouette_euclidean in the k = 2..15 sweep (0.4577; k=11
0.4513, k=13 0.4431, k=9 0.4406).

The peak is interior

The sweep used a single seed, so
the choice is not checked for seed stability.

The fact that k=10 is a coincidence. The number of labels played no role in this.



## Claimed results (must match `results/metrics.json`)
| Metric | Euclidean | Mahalanobis |
|---|---|---|
| Silhouette (common Euclidean) | 0.4577 | 0.4577 |
| Silhouette (configured geometry) | 0.4577 | 0.4577 |
| V-measure | 0.2807 | 0.2807 |
| Accuracy | 0.3271 | 0.3271 |
| Macro F1 | 0.2522 | 0.2522 |

- Primary comparison criterion declared before weight experiments:No weight experiments were run. Not enough time
- The diagonal C you chose, its feature order, and why: C = identity. Identity was left unchanged because no weighting experiment was done
- Same sample, k, seed and restart budget across the primary runs: [ ] [x] (3,730 rows, k=10, seed=42, n_init=30)
- Tradeoffs and whether any independent validation was used:No independent validation was used. All metrics are in-sample

## AI-use acknowledgment
Per the syllabus policy, briefly note any substantive use of AI assistants.

I used Claude (Anthropic) during this project. It advised debugging k selection mahalanobis_sqdist, and structuring this
document. In addition, it helped organise data for the report.