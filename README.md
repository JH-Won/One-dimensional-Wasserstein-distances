# One-dimensional-Wasserstein-distances

This is a code base for my thesis work, the analysis of one-dimensional Wasserstein distances. 

## Introduction

The Wasserstein distance is a well-known distance for capturing domain difference between probability density functions using sample distance information. The use of sample distance has been emphasized widely in various applications, particularly for those having density functions with significantly different domains. However, it has been unclear whether the optimal transport distance encodes rate difference information of density function or completely ignores it. In my thesis, by analyzing the distance of Poisson process signals, I demonstrate the distance actually encodes the rate difference information of signals.

## Core idea and derivation

I use the fact that one-dimensional Wasserstein distance is a linear combination of sample distances. That is, for two Poisson processes $\mu=\{x_1, x_2, \cdots, x_n\}$ and $\nu = \{y_1, y_2, \cdots, y_n\}$ of different rates $\lambda_1$ and $\lambda_2$, the Wasserstein distance is:

$$ W(\mu, \nu) = \frac{1}{n} \sum^n_{k=1} |x_k - y_k|, $$

and the expected information we can obtain from the distance $W(\mu, \nu)$ is a sum of the sample distance expectations:

$$ \mathbb{E}[W(\mu, \nu)] = \frac{1}{n} \sum^n_{k=1} \mathbb{E}[|x_k - y_k|].$$ 

In my thesis, I derive the sample distance expectation $\mathbb{E}[|x_k - y_k|]$ and show that the rate difference between $\lambda_1$ and $\lambda_2$ is indeed encoded in the expectation, which can be viewed as an evidence that the Wasserstein distance can capture the rate difference between density functions.

The derivation of the sample distance expectation is:

$$ \mathbb{E}[|x_k - y_k|] = \int \int |x_k - y_k| p(x_k) p(y_k), $$

where the double integration is taken over $[0, \infty)$, and the density functions of signals $x_k, y_k$ are gamma density functions. The integration yields the result: 

$$ \mathbb{E} [|x_k - y_k|] = \frac{\lambda_1 \lambda_2}{\lambda_1+\lambda_2}\sum_{i=0}^{2k} \binom{2k}{i} \left(\frac{\lambda_1}{\lambda_1+\lambda_2}\right)^{i} \left(\frac{\lambda_2}{\lambda_1+\lambda_2}\right)^{2k-i} |k-i|, $$

which can be, interestingly, rewritten as the following binomail expectation:

$$ \mathbb{E} [|x_k - y_k|] = \frac{\lambda_1 \lambda_2}{\lambda_1+\lambda_2}\mathbb{E}_{i \sim P(i|2k,p)}\left[|k - i|\right], $$

with $P = \frac{\lambda_1}{\lambda_1+\lambda_2}.$

Now, in this expectation, I show the binomial expectation $\mathbb{E}_{i \sim P(i|2k,p)}\left[|k - i|\right]$ is indeed a rate difference between $\lambda_1$ and $\lambda_2$. In other words:

$$ \frac{\partial}{\partial \lambda_1} \mathbb{E}_{i \sim P(i|2k,p)}\left[|k - i|\right] = 0, $$

when $\lambda_1 = \lambda_2.$

# Code

In this repo, I include a python implementation of the derivation ``utils.exp_was_dist`` with the jupyter notebook ``validation.ipynb`` for validating the result.

In the notebook, you can generate the figures that validates the derivation:

### Comparision with the empirical mean:
![Validation result1](https://github.com/JH-Won/One-dimensional-Wasserstein-distances/blob/main/Validation.png)


### Rate encoding of the sample distance:
![Validation result2](https://github.com/JH-Won/One-dimensional-Wasserstein-distances/blob/main/Validation_rate_encoding.png)
