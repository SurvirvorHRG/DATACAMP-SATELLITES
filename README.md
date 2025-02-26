# RAMP starting kit on satellite decay date prediction

Artificial satellites in Earth's orbit do not remain operational indefinitely. Over time, gravitational pull, atmospheric drag, and other factors alter their trajectory, eventually leading to their decay (disintegration). Predicting when a satellite will decay is a critical challenge for managing space traffic, avoiding collisions, and ensuring the safety of orbital infrastructure.

The goal of this RAMP challenge is to design an algorithm that accurately predicts the decay date of satellites using their orbital parameters.

## Getting started

### Install

To run a submission and the notebook you will need the dependencies listed
in `requirements.txt`. You can install the dependencies with the
following command-line:

```bash
pip install -U -r requirements.txt
```

If you are using `conda`, we also provide an `environment.yml` file for similar usage.

### Challenge description

Get started on this RAMP with the
[dedicated notebook](satellites_starting_kit.ipynb).

### Test a submission

The submissions need to be located in the `submissions` folder. For instance
for `my_submission`, it should be located in `submissions/my_submission`.

To run a specific submission, you can use the `ramp-test` command line:

```bash
ramp-test --submission my_submission
```

You can get more information regarding this command line:

```bash
ramp-test --help
```

### To go further

You can find more information regarding `ramp-workflow` in the
[dedicated documentation](https://paris-saclay-cds.github.io/ramp-docs/ramp-workflow/stable/using_kits.html)
