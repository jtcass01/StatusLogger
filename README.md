<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h3 align="center">Status Logger</h3>

  <p align="center">
    Python Status Logger module tested on both Linux and Windows operating systems that provides file logging and colored console log operations.
    <br />
    <a href="https://github.com/jtcass01/StatusLogger"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/jtcass01/StatusLogger/issues">Report Bug</a>
    ·
    <a href="https://github.com/jtcass01/StatusLogger/issues">Request Feature</a>
  </p>
</p>


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>


<!-- GETTING STARTED -->
## Getting Started

1. Clone the repo
  ```Bash
  git clone https://github.com/jtcass01/StatusLogger.git
  ```

### Prerequisites

2. Install 3rd Party Modules
  - Needed for Linux
   ```Bash
   python -m pip install colorama
   ```
  - Needed for Windows
   ```Bash
   python -m pip install printy
   ```

### Installation

3. Install StatusLogger from within StatusLogger directory
   ```Bash
   python -m pip install .
   ```

  or

   ```Bash
   python build.py
   ```

<!-- USAGE EXAMPLES -->
## Usage

- Console Logging
  ```Python
  from StatusLogger.Logger import Logger
  
  Logger.console_log(message="Hello World.", message_type=Logger.MESSAGE_TYPE.SUCCESS)
  ```

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the GPL-3.0 License. See `LICENSE` for more information.


<!-- CONTACT -->
## Contact

Jacob Taylor Cassady - [@Jacob_Cassady](https://twitter.com/Jacob_Cassady) - jacobtaylorcassady@outlook.com

Project Link: [https://github.com/jtcass01/StatusLogger](https://github.com/jtcass01/StatusLogger)
