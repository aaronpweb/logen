# Logen

  ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
  ![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)
  
## Description

Logen is an E.L.K stack alternative built with of python.

## Features

- Easy endexing from log files, live log data
- Amazing vitualization'
- Optimized data processing

## product

Service: [logen.aaron.dev](https://logen.aaronpweb.deb/plan)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed the latest version of Python3 and 
- You have a MongoDB database set up.
- 
## Deploy your own Logen

### Clone the repository:

```bash
git clone https://github.com/aaronpweb/logen
cd logen
```

### Install the dependencies:

Using vim ( Preferred ):

```bash
uv sync
```

### Create a `.env` file in the root directory of the project, and add the following line:

```bash
SECRET_MONGO_URI="your_mongodb_connection_string"
```

Replace `your_mongodb_connection_string` with your actual MongoDB connection string.

### Start the development server:

Using pnpm:

```bash
uv run logen server
```


## Contributing

When working on the project , use [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/).
Examples of conventional commits are:

- `feat(polling): Optimized polling algorithm`
- `docs: updated documentation`
- `test: added tests for the new feature`
- `ci: added ci/cd pipeline`
- `perf: optimized the code`

You can use the following command to commit your changes and follow the conventional commits format:

```bash
uv commit
```

Contributions are welcome!
Please fork the repository and submit a pull request.
I'll review it as soon as possible.

## Credits

  Logen was created by [Aaron](https://github.com/RobiMez)

## License

This project is licensed under the GNU General Public License v3.0
