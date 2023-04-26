# Vrinda-SSH

## About

I am proud to introduce Vrinda-SSH, a tool developed as part of my personal project. The name "Vrinda," which means basil in Sanskrit, was chosen for its connotations of strength and resilience - perfect for an attack tool. Vrinda-SSH is designed to test the security of network by brute-forcing the specified IP address using a provided wordlist via SSH (p22).

One of the key features of Vrinda-SSH is its speed and efficiency, thanks to the inclusion of threading and paralyzation support. While it is still a work in progress and may have some bugs, I have big plans for the future of Vrinda-SSH. In the coming months and years, I hope to add a progress bar, support for key-based and multifactor attacks, and possibly even a GUI.

I am excited to continue developing and improving Vrinda-SSH, and hope that it will become a valuable tool for anyone looking to test the strength of their Network.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/username/vrinda-ssh.git
```

2. Change the directory:

```bash
cd vrinda-ssh
```

3. Install the required packages:
The script will automatically install the required packages when it runs for the first time.

## Usage

To run the script, simply execute the following command:

```bash
python3 vrinda-ssh.py
```

The script will prompt you to provide the following information:

- Path to the users list
- Path to the password list
- Target IP address
- Target port (usually 22 for SSH)

Once you have provided this information, the brute-force attack will begin.

## Disclaimer

This tool is for educational purposes only. The author is not responsible for any misuse or damage caused by this script. Always seek permission before testing on any target.

## Contributing

We welcome contributions to the project. To contribute, please follow these steps:

1. Fork the repository.
2. Create a branch with a descriptive name.
3. Make your changes and commit them to your branch.
4. Create a pull request, detailing the changes you made and the reasons behind them.

For major changes or new features, please open an issue first to discuss what you would like to change.

## License

[MIT License](https://choosealicense.com/licenses/mit/)
