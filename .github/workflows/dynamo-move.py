# This is a basic workflow to help you get started with Actions

name: CI

# Controls when the workflow will run
on:
  pull_request:
    branches: [ preprod ]

  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:

# A workflow run is made up of one or more jobs that can run sequentially or in parallel
jobs:
  # This workflow contains a single job called "build"
  build:
    # The type of runner that the job will run on
    runs-on: ubuntu-latest

    # Steps represent a sequence of tasks that will be executed as part of the job
    steps:
      # Checks-out your repository under $GITHUB_WORKSPACE, so your job can access it
      - uses: actions/checkout@v2
      - name: Set up Python 3.8
        uses: actions/setup-python@v2
        with:
          python-version: 3.8
      # Runs a single command using the runners shell
      - name: Run a one-line script
        run: echo Hello, world!

      # Runs a set of commands using the runners shell
      - name: Run a multi-line script
        run: |
          pip install boto3
          echo Respaldando tabla 1 sia-afore-aims-cat-divisas-dev
          python dynamo-move.py -sa ${{secrets.AWS_KEY_ID_DEVELOP}} -ss ${{secrets.AWS_KEY_SECRET_DEVELOP}} -da ${{secrets.AWS_KEY_ID_PREPROD}} -ds ${{secrets.AWS_KEY_SECRET_PREPROD}} -st sia-afore-aims-cat-divisas-dev -dt sia-afore-aims-cat-divisas-pre 
          echo Respaldando tabla 2 sia-afore-aims-cat-operaciones-dev
          python dynamo-move.py -sa ${{secrets.AWS_KEY_ID_DEVELOP}} -ss ${{secrets.AWS_KEY_SECRET_DEVELOP}} -da ${{secrets.AWS_KEY_ID_PREPROD}} -ds ${{secrets.AWS_KEY_SECRET_PREPROD}} -st sia-afore-aims-cat-operaciones-dev -dt sia-afore-aims-cat-operaciones-pre 
