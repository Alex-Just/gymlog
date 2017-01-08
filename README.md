gymlog
===============================
Source code of gymlog.tk - Web version of your personal workout log

*The project is in its early stages. It can be built and smoke-tested.*

##Build status and test coverage
Front-end: [![Build Status](https://semaphoreci.com/api/v1/alexjust/gymlog-frontend/branches/dev/shields_badge.svg)](https://semaphoreci.com/alexjust/gymlog-frontend) [![Test Coverage](https://codeclimate.com/github/Alex-Just/gymlog/badges/coverage.svg)](https://codeclimate.com/github/Alex-Just/gymlog/coverage) 

Back-end: [![Build Status](https://travis-ci.org/Alex-Just/gymlog.svg?branch=dev)](https://travis-ci.org/Alex-Just/gymlog) [![Coverage Status](https://coveralls.io/repos/github/Alex-Just/gymlog/badge.svg?branch=dev)](https://coveralls.io/github/Alex-Just/gymlog?branch=dev)

##Technology stack

Technology | Path
--- | ---
**Front-end** | 
React + Redux + CSS Modules | src/
Webpack v2 | config/webpack.[env].config.js
Tests: Karma/Mocha/Expect | src/\_\_tests\_\_
**Back-end** |
Django | config/settings/<br>gymlog/
PostgreSQL | 
Tests: pytest | gymlog/users/tests/
Development methodology: BDD | features/
