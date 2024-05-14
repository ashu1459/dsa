<?php

namespace Services\Events;

Interface EventsInterface {
    
    /**
     * @return string
     */
    public function get(): string;

    /**
     * @param string $event
     * 
     * @return void
     */
    public function set($event): void;

    /**
     * @param string $event
     * 
     * @return string|null
     */
    public function getText($event): string|null;
}