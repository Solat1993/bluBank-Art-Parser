# Art Parser

## Notes
- You are not expected to finish everything in an hour - **I couldn't do it**.
- We use Python but feel free to do it in whatever in whatever language you prefer.
- **Please make a new commit for each step.**
- When finished, please push to github and send me a link.

## Before you start:
- Rename this file to `TASKS.md`.
- Initialize an empty repository via `git init .`
- Add `Tasks.md` to `.gitignore`.

## Background

A large part of work in a Data Science Product Team is to transform Data from one format to another. In this challenge you are going to do this on some HTML files. 

## Steps:

In the data directory you'll find a directory called '2015-03-18'. In that folder there are five files, representing five pieces that sold.

**Write a script that parses the HTML files in that directory, extracts the artist names and outputs a JSON array of the unique names to stdout.**

Example:
```
  ['Pablo Picasso', 'Marc Chagall', ...]
```

**Modify your script to extract the title of the work as well. Modify your output format to be an array of objects.**

Example:
```
[
  {
    artist: 'Pablo Picasso',
    works: ['Quatre Femmes nues et Tête sculptée, from: La Suite Vollard' ...],
  },
  ...
]
```
**Modify your script yet again, extracting the price realized and including it alongside the works.**

Example:
```
[
  {
    artist: 'Pablo Picasso',
    works: [
      { title: 'Femme accroupie (Jacqueline)', price: 'USD 25,000' },
      ...
    ],
  },
  ...
]
```
**Modify your script one more time, separating the currency from the amount.**
```
[
  {
    artist: 'Pablo Picasso',
    works: [
      { title: 'Femme accroupie (Jacqueline)', currency: 'GBP', amount: '25,000' },
      ...
    ],
  },
  ...
]
```


**Now look at the directory named: `2017-12-20`. Parse these works into the above structure as well.**

**Convert the amount of all works to USD. Feel free to use the conversion rate of 1GBP = 1.34 USD.**

**Modify your script to return the total sales value for each artist:**

Example:
```
[
  {
    artist: 'Pablo Picasso',
    totalValue: 'USD xxxxxxxxx',
    works: [
      { title: 'Femme accroupie (Jacqueline)', currency: 'USD', totalLifetimeValue '25,000' },
      ...
    ],
  },
  ...
]
```

## Congratulations!
