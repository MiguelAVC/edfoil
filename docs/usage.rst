Usage
=====

.. _installation:

Installation
------------

To use EdFoil, clone the repository:

.. code-block:: console

   (.venv) $ git clone https://github.com/MiguelAVC/edfoil.git

Create a python virtual environment inside the root directory. This can be done in the terminal with the following:

.. code-block:: console

   (.venv) $ python -m venv .venv

Install all the required dependencies with the following commands:

.. code-block:: console

   (.venv) $ source .venv/Scripts/activate  # On Windows use `.venv\Scripts\activate`
   (.venv) $ pip install -r requirements.txt

Run the main script to start using EdFoil:

.. code-block:: console

   (.venv) $ python main.py

.. Creating recipes
.. ----------------

.. To retrieve a list of random ingredients,
.. you can use the ``edfoil.classes.airfoil.Airfoil()`` function:

.. .. autofunction:: edfoil.classes.airfoil.Airfoil()

.. The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
.. or ``"veggies"``. Otherwise, :py:func:`edfoil.classes.airfoil`
.. will raise an exception.

.. For example:

.. >>> import lumache
.. >>> lumache.get_random_ingredients()
.. ['shells', 'gorgonzola', 'parsley']

