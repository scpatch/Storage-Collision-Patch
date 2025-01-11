[toc]

# Debug Tracing Tool

This section focuses on tools and modules designed to trace, debug, and analyze the execution of Ethereum smart contracts.

## EVM Trace

- **Repository**: [evm-trace](https://github.com/ApeWorX/evm-trace)
- **Description**: A library designed for tracing Ethereum Virtual Machine (EVM) execution. It simplifies working with trace logs and provides structured representations of EVM execution frames.
- **Key Features**:
  - Enables detailed inspection of smart contract execution.
  - Supports tracking storage changes, stack state, and memory during transactions.
  - Compatible with multiple Ethereum clients.
- **Module**: `evm-trace`

## Octopus Updated Version

- **Base Tool**: [octopus](https://github.com/FuzzingLabs/octopus)
- **Description**: An extension of the original Octopus tool, updated to support new versions of smart contracts and opcode sets.
- **Key Features**:
  - Enhances compatibility with newer Solidity versions and EVM opcode updates.
  - Adds advanced debugging and instrumentation features for smart contract analysis.
  - Provides automated instrumentation for storage-related operations (e.g., `SSTORE` and `SLOAD`).
- **Use Cases**:
  - Security analysis of modern smart contracts.
  - Debugging upgradeable contracts and ensuring patch consistency.
- **Module**: `octopus-update`

## Runtime Simulator

### Ganache

- **Repository**: [Ganache](https://archive.trufflesuite.com/ganache/)
- **Description**: A personal blockchain for Ethereum development, enabling fast and deterministic testing of smart contracts.
- **Key Features**:
  - Provides a local Ethereum network with customizable settings.
  - Supports transaction tracing, gas usage analysis, and contract deployment testing.
  - Offers integration with Infura to fork the Ethereum mainnet for real-world contract testing.
- **Use Cases**:
  - Simulating transaction execution in isolated environments.
  - Debugging and performance profiling for smart contracts.
- **Module**: `ganache`

## Data Modules

### Experiment Data Storage

- **Description**: Modules to store and organize experimental data used in the paper, focusing on both micro and macro benchmarks.
- **Key Features**:
  - Organized storage for experimental results, enabling easy retrieval and analysis.
  - Support for structured data formats like JSON and CSV.
  - Includes metadata such as execution environment, runtime parameters, and benchmarking results.
- **Use Cases**:
  - Storing micro-benchmark data for opcode-level performance analysis.
  - Maintaining macro-benchmark data for end-to-end system evaluations.
- **Module**: `data-storage`

## Quick-Start Module

### Getting Started with Demo Examples

- **Description**: A module to provide users with a quick-start guide and demo examples to familiarize them with the tools.
- **Demo Example**:
  - Deploy a demo contract using Ganache.
  - Trace a transaction using `evm-trace`.
  - Analyze the execution log with `octopus-update` and patch it.
  - Redeploy and check vulnerability

### Batch-Run Functionality

- **Description**: A feature within the quick-start module to enable batch execution of experiments.
- **Key Features**:
  - Automates the execution of multiple test cases.
  - Supports parallel runs to save time during large-scale benchmarking.
  - Provides aggregated results for batch experiments.
- **Use Cases**:
  - Running all benchmark tests in one go.
  - Comparing results across multiple configurations or contract versions.
