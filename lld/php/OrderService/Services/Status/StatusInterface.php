<?php

namespace Services\Status;

interface StatusInterface {
    
    /**
     * @return string
     */
    public function get(): string;

    /**
     * @param string $status
     * 
     * @return void
     */
    public function set($status): void;

    /**
     * @param string $status
     * 
     * @return string|null
     */
    public function getText($status): string|null;
}