<?php

use Services\Events\EventsConstants;
use Services\Events\EventsInterface;

Class Events implements EventsInterface {
    
    /**
     * @var string
     */
    private $events;

    /**
     * 
     */
    public function __construct() {
        $this->events = EventsConstants::INIT;
    }

    /**
     * @return string
     */
    public function get(): string {
        return $this->events;
    }

    /**
     * @param string $events
     * 
     * @return void
     */
    public function set($events): void {
        $this->events = $events;
    }

    /**
     * @param string $event
     * 
     * @return string|null
     */
    public function getText($event): string|null {

        if (EventsConstants::eventsExists($event)) {
            return $event;
        }

        return null;
    }
}