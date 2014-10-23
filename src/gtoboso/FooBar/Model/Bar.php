<?php

namespace gtoboso\FooBar\Model;

abstract class Bar
{
    /**
     * @var string
     */
    protected $lala;

    public function __construct($lala)
    {
        $this->lala = $lala;
    }

    /**
     * Attempt do anything
     */
    abstract protected function doAnything();
}
