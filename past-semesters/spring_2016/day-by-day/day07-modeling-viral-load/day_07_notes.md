# Overview for Day 07

## In-class Activity: Understanding Parameter-Fitting by Exploring Viral Load

Here we explore a model of the **viral load**—the number of virions in the blood of a patient infected with HIV—after the administration of an antiretroviral drug. One model for the viral load predicts that the concentration $V (t)$ of HIV in the blood at time t after the start of treatment will be:

$$ \begin{equation} V(t) = A \mathrm{exp}(-\alpha t) + B \mathrm{exp}(-\beta t) \label{1}  \end{equation}$$ 

When we write mathematics, $\mathrm{exp}(\dots)$ is notational shorthand for $e^{(\dots)}$. So, we can rewrite the viral load model ($\ref{1}$) if we want to understand that it's exponential:

$$  
\begin{equation}
V(t) = A e\^{(-\alpha t)} + B e\^{(-\beta t)}  
\end{equation}
$$

Two things to note about this particular model: 

1. Viral load **is a function of time $t$**. That's why we're writing it as $V(t) = \dots$. 
2. There are four modeling parameters (numbers) we can vary: $(A, \alpha, B, \beta )$:


$$  
\begin{equation}
V(t) = \textbf{A} e\^{(-\boldsymbol{\alpha} t)} + \textbf{B} e\^{(- \boldsymbol{\beta} t)}  
\end{equation}
$$

## Source

This tutorial is adapted from:

Kinder, Jesse M.; Nelson, Philip (2015-07-01). A Student's Guide to Python for Physical Modeling (pp. 61–64). Princeton University Press. Kindle Edition. 

